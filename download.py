from tqdm import tqdm
import requests

url = "https://archive.org/download/tiny-11-core-x-64-beta-1/tiny11%20core%20x64%20beta%201.iso"
filepath = "tiny11.iso"

# Streaming, so we can iterate over the response.
response = requests.get(url, stream=True)

# Sizes in bytes.
total_size = int(response.headers.get("content-length", 0))
block_size = 1024

with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
    with open(filepath, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

if total_size != 0 and progress_bar.n != total_size:
    raise RuntimeError("Could not download file")