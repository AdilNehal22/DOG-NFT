from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpfulScripts import fundAdvancedCollectible

#deploys the contract and funds it with LINK
def main(): 
    dev = accounts.add(config['wallets']['from_key'])
    publish_source = False 
    print(network.show_active())
    advancedCollectible = AdvancedCollectible.deploy(
        config['networks'][network.show_active()]['vrf_coordinator'],
        config['networks'][network.show_active()]['link_token'],
        config['networks'][network.show_active()]['keyhash'],
        {'from': dev},
        publish_source=publish_source
    )

    fundAdvancedCollectible(advancedCollectible)
    return advancedCollectible