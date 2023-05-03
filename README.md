# TicTacToe on the Algorand blockchain
In this solution I describe how you can develop the Tic-Tac-Toe game on the Algorand blockchain. The game logic is implemented as a [Stateful Smart Contract](https://developer.algorand.org/docs/features/asc1/stateful/) using [PyTeal](https://pyteal.readthedocs.io/en/latest/overview.html) while the communication with the network is done using the [py-algorand-sdk](https://github.com/algorand/py-algorand-sdk). 

Two players submit equal amount of algos to an escrow address which marks the start of the game. After this step, the players interchangeably place their marks on the board where the placing mark action is implemented as an application call to the Stateful Smart Contract. In the end whoever player wins the game is able to withdraw the funds submitted to the escrow address, in case of a tie both players are able to withdraw half of the amount submitted to the escrow address.

The goal of this solution is to present a starting point for developers to easily build board games as DApps on the Algorand Blockchain. The idea is that they should be able to change the game logic from Tic-Tac-Toe to whichever board game they prefer like Chess, Connect4, Go or others and deploy it on the network. 

# Environment setup

- `pip install -r requirements.txt`
- Configure a `config.yml` file with the properties shown below:

```yaml
accounts:
  account_1:
    address: PUBLIC_KEY_VALUE
    mnemonic: MNEMONIC_WORDS
    private_key: PRIVATE_KEY_VALUE
  account_2:
    address: PUBLIC_KEY_VALUE
    mnemonic: MNEMONIC_WORDS
    private_key: PRIVATE_KEY_VALUE
  account_3:
    address: PUBLIC_KEY_VALUE
    mnemonic: MNEMONIC_WORDS
    private_key: PRIVATE_KEY_VALUE
  total: 3

client_credentials:
  address: ADDRESS_VALUE
  token: TOKEN_VALUE

```

# Starting the application

- Once you have setup your config file you will be able to use the UI that is located in the `app.py` file in order to play a game on the Algorand Testnet.
- In order to start the UI you need to be located in the root of the project and run the following command: `streamlit run app.py`
- You can watch the following video that gives a short introduction to the solution as well as how you can play one TicTacToe game on the Algorand TestNet using the UI.

[![Watch the video](https://github.com/Vilijan/TicTacToe_Algorand/blob/main/images/video_bg.png?raw=true)](https://www.youtube.com/watch?v=5FSWJR7fDZY&t=9s&ab_channel=VilijanMonev)
