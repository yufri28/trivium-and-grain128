import trivium
import grain128
import warnings


def main():
    # masukan string key dan vektor inisial
    key_str = "adrian"
    iv_str = "adrian"

    warnings.filterwarnings("ignore", category=UserWarning)
    print("======================================")
    print("========== TRIVIUM =================")
    print("======================================")
    print("==========Plainteks 1==============")
    trivium.plainteks_pertama(key_str, iv_str)
    print("==========END Plainteks 1==============")
    print("==========Plainteks 2==============")
    trivium.plainteks_kedua(key_str, iv_str)
    print("==========END Plainteks 2==============")
    print("==========Plainteks 3==============")
    trivium.plainteks_ketiga(key_str, iv_str)
    print("==========END Plainteks 3==============")
    print("==========Plainteks 4==============")
    trivium.plainteks_keempat(key_str, iv_str)
    print("==========END Plainteks 4==============")
    print("==========Plainteks 5==============")
    trivium.plainteks_kelima(key_str, iv_str)
    print("==========END Plainteks 5==============")

    print("======================================")
    print("========== GRAIN 128 =================")
    print("======================================")
    print("==========Plainteks 1==============")
    grain128.plainteks_pertama(key_str)
    print("==========END Plainteks 1==============")
    print("==========Plainteks 2==============")
    grain128.plainteks_kedua(key_str)
    print("==========END Plainteks 2==============")
    print("==========Plainteks 3==============")
    grain128.plainteks_ketiga(key_str)
    print("==========END Plainteks 3==============")
    print("==========Plainteks 4==============")
    grain128.plainteks_keempat(key_str)
    print("==========END Plainteks 4==============")
    print("==========Plainteks 5==============")
    grain128.plainteks_kelima(key_str)
    print("==========END Plainteks 5==============")


if __name__ == '__main__':
    main()
