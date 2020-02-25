#include "FlightBooking.h"
#include <iostream>

using namespace std;

void FlightBooking::printStatus() {
    cout << "Flight: " << this->id << " : "
         << this->reserved << "/" << this->capacity << "("
         << 100 * this->reserved / this->capacity << "%) reserved seats"  << endl;
}

FlightBooking::FlightBooking(int id, int capacity, int reserved){
    // Save data to members.
    this->id       = id;
    this->capacity = capacity;
    this->reserved = reserved;
}


bool FlightBooking::reserveSeats(int number_of_seats){
    if(this->reserved + number_of_seats <= this->capacity){
        this->reserved += number_of_seats;
        return true;
    } 
    else {
        return false;
    }
}

bool FlightBooking::cancelReservations(int number_of_seats){
    if(this->reserved - number_of_seats >= 0){
        this->reserved -= number_of_seats;

        return true;
    } 
    else {
        return false;
    }
}
