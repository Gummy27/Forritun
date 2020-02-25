#include <iostream>
#include "FlightBooking.h"
#include <string>
#include <sstream>

using namespace std;

int main(){
    FlightBooking bookings[10];
    int id, fjoldi;
    string input, skipun;

    do {
        cout << ">";
        getline(cin, input);

        stringstream ss;
        ss << input;
        ss >> skipun >> fjoldi;

        if(skipun == "add") {
            booking.reserveSeats(fjoldi);
        } else if(skipun == "cancel") {
            booking.cancelReservations(fjoldi);
        } else if(skipun == "print") {
            booking.printStatus();
        }

    } while(skipun != "quit");

    return 0;
}