from brownie import AdvancedCollectible, network, accounts, config
from scripts.helpfulScripts import getBreed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("working on" + network.show_active())
    advancedCollectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    numberOfAdvancedCollectible = advancedCollectible.tokenCounter()
    print("The number of tokens you deployed: " + str(numberOfAdvancedCollectible))
    #loop through all token and check if tokenURI is set properly
    for tokenId in range(numberOfAdvancedCollectible):
        breed = getBreed(advancedCollectible.tokenIdToBreed(tokenId))
        #check if we have already not set tokenURI
        if not advancedCollectible.tokenURI(tokenId).startswith("https://"):
            print("setting token URI of {}".format(tokenId))
            setTokenURI(tokenId, advancedCollectible, dog_metadata_dic[breed])
        else:
            print("skipping {}, we have already set that token URI".format(tokenId))

def setTokenURI(tokenId, nftContract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nftContract.setTokenURI(tokenId, tokenURI, {"from": dev})
    print(
        #opensee format
        "You can see your NFT here {}".format(
            OPENSEA_FORMAT.format(nftContract.address, tokenId)
        )
    )
    print('wait 20 minutes, and hit the "refresh metadata" button')