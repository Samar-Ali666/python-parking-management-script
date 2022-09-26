bookings = []

maxParkingSpace = 20
continueProgram = True


def getRequestedDay():
    requestedDay = int(input('Enter the day between (1 - 14): \n'))

    while requestedDay < 0 or requestedDay > 14:
        print('Invalid Day! Kindly enter valid Day')
        requestedDay = int(input('Enter the day between (1 - 14): \n'))

    return requestedDay


def getCarLicence():
    carLicence = input('Enter the licence number: \n')

    while not carLicence.isalnum():
        print('Invalid Licence! Special character are not allowed')
        carLicence = input('Enter the licence number: \n')

    return carLicence


def getVisitorName():
    visitorName = input('Enter the visitor name: \n')

    while not all(name.isalpha() or name.isspace() for name in visitorName):
        print('Invalid Name! Name should contain only alphabets')
        visitorName = input('Enter the visitor name: \n')

    return visitorName


def checkSpaceAvailability(requestedDay):
    spaces_occupied_at_requestedDay = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay:
            spaces_occupied_at_requestedDay += 1

    if spaces_occupied_at_requestedDay >= maxParkingSpace:
        return -1

    return spaces_occupied_at_requestedDay


def isAccessibleParking():
    parkingType = input('Do you want accessible parking spaces? (yes/no): \n')

    if parkingType == 'yes':
        return True
    else:
        return False


def assignGeneralSpace(visitorName, licence, requestedDay):
    generalSpaceNumber = 20

    for booking in bookings:
        if booking['requestedDay'] == requestedDay and booking['parkingNumber'] != generalSpaceNumber:
            generalSpaceNumber = maxParkingSpace
        else:
            generalSpaceNumber = generalSpaceNumber - 1

    createBooking(visitorName, licence, requestedDay, generalSpaceNumber)


def assignAccessibleSpace(visitorName, licence, requestedDay):
    accessibleSpaceNumber = checkSpaceAvailability(requestedDay)

    createBooking(visitorName, licence, requestedDay,
                  accessibleSpaceNumber + 1)


def createBooking(visitorName, licence, requestedDay, parkingNumber):
    newBooking = {}
    newBooking['visitorName'] = visitorName
    newBooking['licence'] = licence
    newBooking['requestedDay'] = requestedDay
    newBooking['parkingNumber'] = parkingNumber

    bookings.append(newBooking)


while continueProgram:
    requestedDay = getRequestedDay()
    parkingSpace = checkSpaceAvailability(requestedDay)

    if parkingSpace != -1:
        accessibleParking = isAccessibleParking()
        visitorName = getVisitorName()
        carLicence = getCarLicence()

        if accessibleParking:
            assignAccessibleSpace(visitorName, carLicence, requestedDay)
        else:
            assignGeneralSpace(visitorName, carLicence, requestedDay)

        print(bookings)

        # print('Parking has been reserved! \nDay ' + str(requestedDay) +
        #       '\nParking number: ' + str(parkingSpace + 1))

        continueProgram = input('Continue (yes/no): \n')
        continueProgram = False if continueProgram == 'no' else continueProgram
    else:
        print('No Spaces available at requeted Day! Select Another day \n')
