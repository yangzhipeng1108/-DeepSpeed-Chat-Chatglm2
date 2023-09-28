# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team

import argparse
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        type=str,
                        help="Directory containing trained actor model")
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=128,
        help="Maximum new tokens to generate per response",
    )
    args = parser.parse_args()

    cmd = f"python3 ./inference/chatbot.py --path {args.path} --max_new_tokens {args.max_new_tokens}"
    p = subprocess.Popen(cmd, shell=True)
    p.wait()


{'input_ids': tensor([[64790, 64792,   790, 30951,   517, 30910, 30939, 30996,    13,    13,
         54761, 31211, 31750, 34904,  4800, 30956, 55249, 57780, 31514,    13,
            13, 55437, 31211, 30910, 31665, 35946, 31623, 17620, 34899, 54774,
         31040,  6489,  1214, 31002, 32159, 31645, 32675, 30994, 30967, 30933,
         30939, 30967,   957, 30919,  2409, 30967, 15383, 31040, 31123, 48310,
         31040, 11800,  3324, 31040, 54542, 31040,   320, 31040, 36395, 31123,
         31756, 31040, 11800,  3324, 31040, 54541, 37325, 31671,  2123, 31123,
         31040,   320, 31040, 54541,  4800, 30956, 55249, 57780,  2123, 31155,
             2],
        [64790, 64792,   790, 30951,   517, 30910, 30939, 30996,    13,    13,
         54761, 31211, 35318, 55153, 55208, 55083, 31514,    13,    13, 55437,
         31211, 30910, 55153, 55208, 55083, 32419, 32066, 38770, 34899, 36622,
         34899, 38503, 54840, 54585, 55396, 38107, 31123, 31779, 55153, 55208,
         55396, 54815, 31201, 54376, 37167, 33400, 54542, 31740, 32066, 33339,
         54609, 31155, 31623, 54376, 37167, 48763, 32994, 34101, 31623, 55153,
         55208, 31155,     2,     0,     0,     0,     0,     0,     0,     0,
             0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
             0]], device='cuda:0'), 'labels': tensor([[ -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100,  -100,  -100, 30910, 31665, 35946, 31623, 17620, 34899, 54774,
         31040,  6489,  1214, 31002, 32159, 31645, 32675, 30994, 30967, 30933,
         30939, 30967,   957, 30919,  2409, 30967, 15383, 31040, 31123, 48310,
         31040, 11800,  3324, 31040, 54542, 31040,   320, 31040, 36395, 31123,
         31756, 31040, 11800,  3324, 31040, 54541, 37325, 31671,  2123, 31123,
         31040,   320, 31040, 54541,  4800, 30956, 55249, 57780,  2123, 31155,
             2],
        [ -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100, 30910, 55153, 55208, 55083, 32419, 32066, 38770, 34899, 36622,
         34899, 38503, 54840, 54585, 55396, 38107, 31123, 31779, 55153, 55208,
         55396, 54815, 31201, 54376, 37167, 33400, 54542, 31740, 32066, 33339,
         54609, 31155, 31623, 54376, 37167, 48763, 32994, 34101, 31623, 55153,
         55208, 31155,     2,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,  -100,
          -100]], device='cuda:0')}