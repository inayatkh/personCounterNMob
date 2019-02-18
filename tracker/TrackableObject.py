'''

Here I defined a class for an object to be tracked in a video or live stream.

This class is used to track and count object and therefore store the information regarding the object such as

an Object unique ID
an Object previous Centroid, for computing the direction of its movement
is the object has already been counted
'''


class TrackableObject:

    def __init__(self, id, centroid):
        '''
        :param id:  object ID
        :param centroid:  current centroid

        Constructor accepts an  Id and centroid and stores them

        '''

        self.objID = id  # stores the objects ID

        self.centroids = [centroid]  # initializes a list of centroids using the current centroid

        self.isAlreadyCounted = False  # initialize a boolean for indication that if the object has been already counted yet or not
