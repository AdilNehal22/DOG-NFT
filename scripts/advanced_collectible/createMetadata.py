from brownie import AdvancedCollectible, network
from metadata import sampleMetadata
from scripts.helpfulScripts import getBreed
from pathlib import Path
import os
import requests
import json
# for assigning the right tokenID to breed


def main():
    print('working on' + network.show_active())
    advancedCollectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    numberOfTokens = advancedCollectible.tokenCounter()
    print('number of tokens you deployed is {}'.format(numberOfTokens))
    writeMetadata(numberOfTokens, advancedCollectible)

# for getting the tokenURI for every


def writeMetadata(numberOfTokens, nftContract):
    for tokenId in range(numberOfTokens):
        collectibleMetadata = sampleMetadata.metadata_template
        breed = getBreed(nftContract.tokenIdToBreed(tokenId))
        metadataFileName = "./metadata/{}/".format(
            network.show_active()) + str(tokenId) + "-" + breed + ".json"

        # if already have metadata
        if Path(metadataFileName).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            print("creating metadata filename {}".format(metadataFileName))
            collectibleMetadata["name"] = getBreed(
                nftContract.tokenIdToBreed(tokenId))
            collectibleMetadata["description"] = "An adorable {} pup".format(
                collectibleMetadata["name"])
            imageToUpload = None
            # if env variable is true
            if os.getenv("UPLOAD_IPFS") == "true":
                imagePath = "./img/{}.png".format(
                    breed.lower().replace("_", "-"))
                imageToUpload = uploadToIPFS(imagePath)
            collectibleMetadata["image"] = imageToUpload
            #dump jsonObject(collectibleMetadata) into metadataFileName
            with open(metadataFileName, "w") as file:
                json.dump(collectibleMetadata, file)
            if(os.getenv("UPLOAD_IPFS")) == "true":
                uploadToIPFS(metadataFileName)

# http://127.0.0.1:5001/webui
# curl -X POST -F file=@img/pug.png http://localhost:5001/api/v0/add now in python


def uploadToIPFS(filePath):
    with Path(filePath).open("rb") as fp:
        imageBinary = fp.read()
        ipfsURL = "http://localhost:5001"
        response = requests.post(
            ipfsURL + "/api/v0/add", files={"file": imageBinary})
        ipfsHash = response.json()["Hash"]
        #will get the name of the filepath
        filename = filePath.split("/")[-1:][0]
        URI = "https://ipfs.io/ipfs/{}?filename={}".format(ipfsHash, filename)
        return(URI)
    return None