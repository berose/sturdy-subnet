# The MIT License (MIT)
# Copyright © 2023 Syeam Bin Abdullah

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import typing
from sturdy.utils.misc import randrange_float, format_num_prec
from sturdy.constants import *


# TODO: add different interest rate models in the future - we use a single simple model for now
def generate_assets_and_pools() -> typing.Dict:  # generate pools
    assets_and_pools = {}
    pools = {
        str(x): {
            "pool_id": str(x),
            "base_rate": randrange_float(MIN_BASE_RATE, MAX_BASE_RATE, BASE_RATE_STEP),
            "base_slope": randrange_float(MIN_SLOPE, MAX_SLOPE, SLOPE_STEP),
            "kink_slope": randrange_float(
                MIN_KINK_SLOPE, MAX_KINK_SLOPE, SLOPE_STEP
            ),  # kink rate - kicks in after pool hits optimal util rate
            "optimal_util_rate": randrange_float(
                MIN_OPTIMAL_RATE, MAX_OPTIMAL_RATE, OPTIMAL_UTIL_STEP
            ),  # optimal util rate - after which the kink slope kicks in
            "borrow_amount": format_num_prec(
                POOL_RESERVE_SIZE
                * randrange_float(
                    MIN_UTIL_RATE,
                    MAX_UTIL_RATE,
                    UTIL_RATE_STEP,
                )
            ),  # initial borrowed amount from pool
            "reserve_size": POOL_RESERVE_SIZE,  # TODO: what should we set reserve size to?
        }
        for x in range(NUM_POOLS)
    }

    assets_and_pools["total_assets"] = TOTAL_ASSETS
    assets_and_pools["pools"] = pools

    return assets_and_pools
