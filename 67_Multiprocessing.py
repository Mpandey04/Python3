import multiprocessing
import requests
import os


def download_file(url, name):
    response = requests.get(url)

    with open(f"Images/img{name}.jpg", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    os.makedirs("Images", exist_ok=True)

    url = "https://picsum.photos/200/300"

    processes = []

    for i in range(5):
        p = multiprocessing.Process(
            target=download_file,
            args=(url, i)
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("All images downloaded successfully!")