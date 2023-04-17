url_origem = 'https://opensea.io/rankings?sortBy=one_day_volume'
string_conexao = 'mysql+mysqlconnector://root:root@localhost/webScraping'

raspagem = [['16', 'Pudgy Penguins', '171 ETH', '-46%', '4.33 ETH', '41', '52%', '3%', '20230413'], ['32', 'CyberBrokers', '79 ETH', '+150%', '0.49 ETH', '146', '32%', '3%', '20230413'], ['40', 'Antidote', '66 ETH', '&lt; 0.01 ETH', '4.803', '37%', '22%', '20230413'], ['48', 'Redacted Remilio Babies', '48 ETH', '-53%', '0.37 ETH', '127', '21%', '3%', '20230413'], ['52', 'adidas Originals Into the Metaverse', '38 ETH', '+46%', '0.76 ETH', '61', '74%', '20230413'], ['56', 'Normies', '32 ETH', '+228%', '65 MATIC', '824', '46%', '15%', '20230413'], ['58', '10KTF Stockroom', '31 ETH', '-4%', '0.06 ETH', '44', '21%', '20230413'], ['60', '0N1 Force', '29 ETH', '+270%', '0.75 ETH', '42', '48%', '3%', '20230413'], ['62', 'World of Women', '28 ETH', '+96%', '1.24 ETH', '24', '56%', '2%', '20230413'], ['63', 'Future Realities: tfoust10 x Reddit Collectible Avatars', '28 ETH', '+6%', '0.06 ETH', '689', '63%', '9%', '20230413'], ['61', 'Valhalla', '28 ETH', '-10%', '0.69 ETH', '41', '34%', '4%', '20230413'], ['59', 'RTFKT Clone X Forging SZN 1 (PRE-FORGE) ⚒️', '31 ETH', '-46%', '0.02 ETH', '84', '31%', '20230413'], ['57', 'OnChainMonkey', '31 ETH', '+29%', '1.85 ETH', '18','32%', '2%','20230413'], ['54', 'y00ts', '37 ETH', '-50%', '2.11 ETH', '17', '10%', '3%', '20230413'], ['55', 'Trump Digital Trading Cards', '36 ETH', '+288%', '0.38 ETH', '96', '31%', '3%', '20230413'], ['53', 'Sappy Seals', '37 ETH', '-38%', '0.68 ETH', '53', '21%', '2%', '20230413'], ['50', 'a KID called BEAST', '38 ETH', '+66%', '0.85 ETH', '36', '39%', '6%', '20230413'], ['51', 'Invisible Friends', '38 ETH', '-1%', '1.62 ETH', '23', '77%', '4%', '20230413'], ['49', 'RENGA', '39 ETH', '-29%', '0.70 ETH', '40', '37%', '7%', '20230413'], ['44', 'ETHEREALS WTF', '60 ETH', '&lt; 0.01 ETH', '12', '31%', '0.6%', '20230413'], ['46', 'YOU THE REAL MVP', '59 ETH', '69.42 ETH', '1', '66%', '0.24%', '20230413'], ['47', 'Kubz', '53 ETH', '-21%', '1.28 ETH', '43', '26%', '0.9%', '20230413'], ['45', 'Opepen Edition', '59 ETH', '-57%', '0.43 ETH', '133', '30%', '2%', '20230413'], ['42', 'Seizon', '62 ETH', '+43%', '0.18 ETH', '347', '28%', '6%', '20230413'], ['43', 'rektguy', '60 ETH', '+331%', '0.75 ETH', '77', '40%', '3%', '20230413'], ['41', 'mfers', '63 ETH', '+61%', '0.86 ETH', '70', '55%', '3%', '20230413'], ['36', 'RTFKT Animus Egg 🥚', '69 ETH', '+505%', '0.44 ETH', '160', '43%', '0.48%', '20230413'], ['38', 'Otherside Vessels', '68 ETH', '-42%', '0.32 ETH', '164', '31%', '1%', '20230413'], ['39', 'The Cultist Club', '67 ETH', '&lt; 0.01 ETH', '5.963', '27%', '12%', '20230413'], ['37', 'Moonbirds', '69 ETH', '+70%', '3.27 ETH', '22', '65%', '0.65%', '20230413'], ['34', 'Kanpai Pandas', '73 ETH', '+100%', '1.53 ETH', '46', '26%', '3%', '20230413'], ['35', 'Saved Souls', '70 ETH', '-36%', '0.05 ETH', '1.385', '26%', '6%', '20230413'], ['33', 'Just a Basic Profile Picture', '78 ETH', '-38%', '0.06 ETH', '920', '27%', '12%', '20230413'], ['24', 'CryptoPunks V1 (wrapped)', '119 ETH', '-51%', '4.55 ETH', '27', '25%', '3%', '20230413'], ['28', 'Fidenza by Tyler Hobbs', '93 ETH', '62 ETH', '2', '47%', '4%', '20230413'], ['30', 'Pixelmon - Generation 1', '83 ETH', '+28%', '0.74 ETH', '88', '28%', '3%', '20230413'], ['31', 'Checks - VV Edition', '80 ETH', '-54%', '0.64 ETH', '121', '37%', '2%', '20230413'], ['29', 'Mint Pass Tokyo AI Collection | Bright Moments | MPAI', '84 ETH', '+816%', '0.35 ETH', '105', '26%', '12%', '20230413'], ['26', 'Blocky Doge 3', '99 ETH', '-86%', '0.03 ETH', '2.157', '34%', '13%', '20230413'], ['27', 'Meebits', '96 ETH', '-67%', '2.64 ETH', '37', '33%', '2%', '20230413'], ['25', 'Terraforms by Mathcastles', '115 ETH', '+871%', '2 ETH', '61', '19%', '1%', '20230413'], ['20', 'PIXELATED HORRORS - An Art Collective', '134 ETH', '+689%', '0.03 ETH', '35', '75%', '4%', '20230413'], ['22', 'NFT Worlds', '125 ETH', '+905%', '1.75 ETH', '66', '9%', '0.73%', '20230413'], ['23', 'ALTS by adidas', '119 ETH', '+41%', '0.78 ETH', '180', '56%', '1%', '20230413'], ['21', 'Doodles', '128 ETH', '-39%', '2.70 ETH', '47', '54%', '3%', '20230413'], ['18', 'HV-MTL', '152 ETH', '+11%', '1.79 ETH', '62', '38%', '3%', '20230413'], ['19', 'Otherdeed Expanded', '134 ETH', '+18%', '0.96 ETH', '99', '32%', '3%', '20230413'], ['17', 'DeGods', '156 ETH', '+1%', '9.35 ETH', '18', '10%', '2%', '20230413'], ['8', 'CLONE X - X TAKASHI MURAKAMI', '519 ETH', '+3%', '2.75 ETH', '193', '49%', '3%', '20230413'], ['12', 'Otherdeed for Otherside', '259 ETH', '-43%', '1.46 ETH', '163', '32%', '2%', '20230413'], ['14', 'Gemesis', '183 ETH', '-61%', '0.05 ETH', '1.347', '52%', '5%', '20230413'], ['15', 'The Potatoz', '179 ETH', '-17%', '3.33 ETH', '54', '30%', '0.61%', '20230413'], ['13', 'Milady Maker', '185 ETH', '-60%', '1.95 ETH', '94', '33%', '3%', '20230413'], ['10', 'Nakamigos', '404 ETH', '-39%', '0.69 ETH', '527', '29%', '12%', '20230413'], ['11', 'The Weirdo Ghost Gang', '279 ETH', '+919%', '0.71 ETH', '443', '36%', '2%', '20230413'], ['9', 'Otherside Koda', '465 ETH', '+273%', '9.20 ETH', '51', '62%', '6%', '20230413'], ['4', 'Mutant Ape Yacht Club', '1.245 ETH', '+80%', '13.05 ETH', '95', '58%', '2%', '20230413'], ['6', 'Bored Ape Kennel Club', '945 ETH', '+18%', '6.03 ETH', '157', '57%', '2%', '20230413'], ['7', 'The Captainz', '643 ETH', '-20%', '7.09 ETH', '87', '47%', '0.7%', '20230413'], ['5', 'BEANZ Official', '1.098 ETH', '+362%', '1.53 ETH', '695', '37%', '2%', '20230413'], ['2', 'Wrapped Cryptopunks', '5.047 ETH', '-16%', '74.83 ETH', '89', '18%', '0.13%', '20230413'], ['3', 'Azuki', '1.927 ETH', '-35%', '15 ETH', '130', '48%', '3%', '20230413'], ['1', 'Bored Ape Yacht Club', '5.606 ETH', '+302%', '55.29 ETH', '100', '57%', '3%', '20230413']]