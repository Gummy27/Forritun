#pragma once

class FlightBooking {
    public:
        FlightBooking(int id, int capacity, int reserved);
        bool reserveSeats(int number_of_seats);
        bool cancelReservations(int number_of_seats);
        void printStatus();
    private:
        int id, capacity, reserved;
};