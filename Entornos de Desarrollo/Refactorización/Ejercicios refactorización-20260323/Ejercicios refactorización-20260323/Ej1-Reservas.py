class ReservationSystem:
    def __init__(self):
        self.reservations = []
        self.customers = []
        self.rooms = []

    def add_reservation(self, customer_name, room_number, check_in, check_out):
        # Validación de fechas
        if check_in >= check_out:
            raise ValueError("Check-in debe ser antes de check-out")
        
        # Verificar disponibilidad
        for res in self.reservations:
            if res.room == room_number:
                if not (check_out <= res.check_in or check_in >= res.check_out):
                    raise ValueError("Habitación no disponible")

        # Calcular precio
        price_per_night = 100
        nights = (check_out - check_in).days
        total = nights * price_per_night

        # Crear reserva
        reservation = {
            'customer': customer_name,
            'room': room_number,
            'check_in': check_in,
            'check_out': check_out,
            'total': total,
            'status': 'confirmed'
        }
        self.reservations.append(reservation)
        
        # Enviar email de confirmación
        import smtplib
        server = smtplib.SMTP('smtp.hotel.com')
        server.sendmail('reservas@hotel.com', f"{customer_name}@email.com", 
                       f"Reserva confirmada: ${total}")
        
        # Actualizar inventario
        self.rooms[room_number]['available'] = False
        
        # Guardar en base de datos
        db.execute("INSERT INTO reservations VALUES (?, ?, ?, ?, ?)",
                  (customer_name, room_number, check_in, check_out, total))
        
        # Generar factura
        self.generate_invoice(customer_name, room_number, total)
        
        return reservation

    def generate_invoice(self, customer, room, total):
        print("=" * 50)
        print(f"FACTURA - {customer}")
        print(f"Habitación: {room}")
        print(f"Total: ${total}")
        print("=" * 50)
    
    def cancel_reservation(self, reservation_id):
        # Buscar reserva
        for res in self.reservations:
            if res['id'] == reservation_id:
                res['status'] = 'cancelled'
                
                # Calcular reembolso
                refund = res['total'] * 0.8
                
                # Actualizar habitación
                self.rooms[res['room']]['available'] = True
                
                # Enviar email de cancelación
                import smtplib
                server = smtplib.SMTP('smtp.hotel.com')
                server.sendmail('reservas@hotel.com', f"{res['customer']}@email.com",
                               f"Cancelación - Reembolso: ${refund}")
                
                # Registrar en base de datos
                db.execute("UPDATE reservations SET status=?, refund=? WHERE id=?",
                          ('cancelled', refund, reservation_id))
                
                return {'success': True, 'refund': refund}
        
        return {'success': False, 'error': 'Reserva no encontrada'}