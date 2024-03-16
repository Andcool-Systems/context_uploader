import sys
import fileuploader
import webbrowser
import asyncio


async def upload():
    filename = sys.argv[1].replace("\\", "/").split("/")
    response = await fileuploader.upload(bytes=open(sys.argv[1], "rb"), filename=filename[-1])
    url = response.file_url_full
    webbrowser.open(url, new=0, autoraise=True)


def main():
    if len(sys.argv) > 1:
        asyncio.run(upload())
    else:
        print("No file path provided.")


if __name__ == "__main__":
    main()