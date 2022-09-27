bookings = [
    {
        "visitorName": "John Doe",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 5
    },
    {
        "visitorName": "John Doe",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 2
    },
    {
        "visitorName": "Williams Smith",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 4
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 4,
        "parkingNumber": 8
    },
    {
        "visitorName": "Rico Suave",
        "licence": "HJHDKFHD679787",
        "requestedDay": 6,
        "parkingNumber": 2
    },
]

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


def showStats():
    userInput = input('1) Add Booking \n2) Show Stats: \n')

    if userInput == '2':
        return True
    elif userInput == '1':
        return False


def showStatsOptions():
    print('Choose the stats you want to see \n')
    print('1) See numbers of accessible spaces used any of the 14 days \n')

    userInput = input()

    if userInput == '1':
        showSingleDayAccessibleStats()


def showSingleDayAccessibleStats():
    requestedDay = int(input(
        'Enter the day you want to See the accessible stats: \n'))

    accessibleSpacesOnRequestedDay = 0

    for booking in bookings:
        if booking["requestedDay"] == requestedDay and booking['parkingNumber'] <= 5:
            accessibleSpacesOnRequestedDay += 1

    print('Total Accessible spaces used: ' +
          str(accessibleSpacesOnRequestedDay))


def createBooking(visitorName, licence, requestedDay, parkingNumber):
    newBooking = {}
    newBooking['visitorName'] = visitorName
    newBooking['licence'] = licence
    newBooking['requestedDay'] = requestedDay
    newBooking['parkingNumber'] = parkingNumber

    bookings.append(newBooking)


while continueProgram:

    isShowStats = showStats()

    if not isShowStats:
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

    else:
        showStatsOptions()
