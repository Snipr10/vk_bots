from pyppeteer import chromium_downloader

DEFAULT_CHROMIUM_VERSION = '588429'


def set_chromium_version(chromium_version):
    if not chromium_version:
        chromium_version = DEFAULT_CHROMIUM_VERSION

    chromium_downloader.REVISION = chromium_version

    chromium_downloader.downloadURLs = {
        'linux': f'{chromium_downloader.BASE_URL}/Linux_x64/{chromium_downloader.REVISION}/chrome-linux.zip',
        'mac': f'{chromium_downloader.BASE_URL}/Mac/{chromium_downloader.REVISION}/chrome-mac.zip',
        'win32': f'{chromium_downloader.BASE_URL}/Win/{chromium_downloader.REVISION}/{chromium_downloader.windowsArchive}.zip',
        'win64': f'{chromium_downloader.BASE_URL}/Win_x64/{chromium_downloader.REVISION}/{chromium_downloader.windowsArchive}.zip',
    }

    chromium_downloader.chromiumExecutable = {
        'linux': chromium_downloader.DOWNLOADS_FOLDER / chromium_downloader.REVISION / 'chrome-linux' / 'chrome',
        'mac': chromium_downloader.DOWNLOADS_FOLDER / chromium_downloader.REVISION / 'chrome-mac' / 'Chromium.app' / 'Contents' / 'MacOS' / 'Chromium',
        'win32': chromium_downloader.DOWNLOADS_FOLDER / chromium_downloader.REVISION / chromium_downloader.windowsArchive / 'chrome.exe',
        'win64': chromium_downloader.DOWNLOADS_FOLDER / chromium_downloader.REVISION / chromium_downloader.windowsArchive / 'chrome.exe',
    }


def revert_to_original_chromium_version():
    set_chromium_version(DEFAULT_CHROMIUM_VERSION)


def download_chromium(chromium_version=None):
    try:
        set_chromium_version(chromium_version)
        if not chromium_downloader.check_chromium():
            chromium_downloader.download_chromium()
    finally:
        revert_to_original_chromium_version()
