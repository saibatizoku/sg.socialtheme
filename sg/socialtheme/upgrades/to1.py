from Products.CMFCore.utils import getToolByName

def install_browser_stuff(context):
    """Re-import jsregistry items to pick up new javscript file"""
    gs = getToolByName(context, 'portal_setup')
    profile = 'sg.socialtheme:default'
    gs.runImportStepFromProfile(profile, 'browserlayer', purge_old=False)
    gs.runImportStepFromProfile(profile, 'cssregistry', purge_old=False)
    gs.runImportStepFromProfile(profile, 'jsregistry', purge_old=False)
