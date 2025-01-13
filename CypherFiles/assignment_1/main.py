from utils import CypherUtils as cyu

def main():
    print("Starting application...")
    cypher_1: list = ["Rkcrevrapr vf gur grnpure bs nyy guvatf. - Whyvhf Pnrfne"]

    cypher_2: list = ["Doha dl dpzo, dl ylhkpsf ilsplcl, huk doha dl vbyzlsclz aopur, dl pthnpul vaolyz aopur hszv. - Qbspbz Jhlzhy"]

    cypher_2 = cyu.transform_to_lower(cypher_2)
    print(cyu.display_frequency(cyu.sort_frequency(cyu.keep_alpha(cyu.frequency(cypher_2)))))

    print(cyu.frequency_bigrams(cyu.transform_to_lower(cypher_1)))

if __name__ == "__main__":
    main()