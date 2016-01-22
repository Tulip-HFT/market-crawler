#!/usr/bin/env python2

import json
import functools

from hitbtc import Hitbtc
from btce import Btce
from itbit import Itbit
from btcchina import Btcchina
from cexio import Cexio
from bter import Bter
from cryptsy import Cryptsy
from kraken import Kraken
from mintpal import Mintpal
from bitfinex import Bitfinex
from okcoincom import Okcoincom
from okcoincn import Okcoincn
from coincheck import Coincheck
from bitstamp import Bitstamp

sort_rank = dict((v, k) for k, v in enumerate(['usd', 'eur', 'cny', 'jpy', 'btc', 'ltc', 'doge']))

def get_sort_rank(currency):
    return sort_rank.get(currency, 999)

def sort_markets(markets):
    def key(market):
        primary, secondary = market.partition('/')[::2]
        return (get_sort_rank(secondary), secondary, get_sort_rank(primary), primary)

    return sorted(markets, key=key )

def main():
    crawlers = [
        Hitbtc(), Btce(), Itbit(), Btcchina(), Cexio(), Bter(), Cryptsy(), Kraken(), Bitfinex(),
        Okcoincom(), Okcoincn(), Coincheck(), Bitstamp()
        # Mintpal()
    ]

    markets = {}
    for crawler in crawlers:
        print crawler.exchange_name()
        markets[crawler.exchange_name()] = sort_markets(crawler.markets())

    for k, v in markets.items():
        print k, len(v)
        # print v

    with open('markets.json', 'w') as fp:
        json.dump(markets, fp, sort_keys=True, indent=4)

if __name__ == '__main__':
    main()
