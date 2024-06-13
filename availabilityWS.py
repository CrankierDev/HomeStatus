from flask import Flask
from enum import Enum, EnumMeta


########################## DEFINE STATUSES ####################################
class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True    


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class Status(BaseEnum):
	KO = 'RED'
	OK = 'GREEN'


########################## DEFINE GLOBALS ######################################
app = Flask(__name__)
USERS = {
	1: Status.OK,
	2: Status.OK
}


########################## DEFINE METHODS ######################################
@app.route('/status/<int:userNumber>/')
def getStatus(userNumber=4):
	print(userNumber)
	if userNumber in USERS:
		return USERS[userNumber].value
	
	else:
		return 'ERROR'


@app.route('/setStatus/<int:userNumber>/<string:status>/')
def setStatus(userNumber, status):
	global USERS
	status = status.upper()

	if userNumber not in USERS:
		return 'ERROR'

	print(USERS[userNumber].value)
	print("STATUS", status, Status[status] in Status)

	if Status[status] in Status:
		print(Status[status])
		USERS[userNumber] = Status[status]

	print(USERS[userNumber].value)
	return 'OK'


########################## START APP ######################################
if __name__ == '__main__':
	app.run()