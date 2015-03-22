from tools.item_share.ItemShareView import (ItemShareView, )

class ToolManager:
    @staticmethod
    def getTools(event):
        eventType = event.eventType
        # TODO (Susan) - Add Database Trip to allow customization of tools for trips.
        # The cases below are the defaults.
        if (eventType == 'Dinner'):
            return (ItemShareView, )
        elif (eventType == 'Hike'):
            return (ItemShareView, )
        elif (eventType == 'Other Trip'):
            return (ItemShareView, )
        elif (eventType == 'Other Gathering'):
            return (ItemShareView, )
        else:
            return (ItemShareView, )
            # TODO - throw error

