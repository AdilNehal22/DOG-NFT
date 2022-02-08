from brownie import AdvancedCollectible, accounts, config, interface, network


def fundAdvancedCollectible(nftContract):
    dev = accounts.add(config['wallets']['from_key'])
    # getting the ABI
    link_token = interface.LinkTokenInterface(
        config['networks'][network.show_active()]['link_token'])
    link_token.transfer(nftContract, 1000000000000000000, {'from': dev})


def getBreed(breedNumber):
    switch = {0: 'PUG', 1: 'SHIBA_INU', 2: 'ST_BERNARD'}
    return switch[breedNumber]