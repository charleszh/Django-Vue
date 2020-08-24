from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

    def getSectionData(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal section")

    def getSectionData(self):
        print("Profile section data")
        self.data = ''


class AlbumSection(Section):
    def describe(self):
        print("Album Section")

    def getSectionData(self):
        print("Profile Album section data")
        self.data = ''


class DataCollectionSection(Section):
    def describe(self):
        print("Data Collection")

    def getSectionData(self):
        print("Profile data count data")
        self.data = ''

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        section.getSectionData()
        self.sections.append(section)


class PlatformProfile(Profile):
    def createProfile(self):
        self.addSections(PersonalSection)
        self.addSections(DataCollectionSection)
