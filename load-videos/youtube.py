import yt_dlp as youtube_dl


def pixel_area(resolution):
    if resolution == "audio only":
        return 0

    width, height = resolution.split("x")
    return int(width)*int(height)


class YoutubeVideo:
    def __init__(self, url):
        self.url = url
        self.data = None

        with youtube_dl.YoutubeDL() as ydl:
            self.data = ydl.extract_info(self.url, download=False)

    def getbest(self):
        formats = self.data["formats"]
        best_version = formats[0]
        best_pixel_area = pixel_area(best_version["resolution"])

        for version in formats:
            resolution = version["resolution"]
            area = pixel_area(resolution)

            if area > best_pixel_area:
                best_version = version
                best_pixel_area = area

        return best_version
