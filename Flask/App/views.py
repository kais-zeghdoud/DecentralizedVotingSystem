import sys, subprocess, logging

from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
from .ganache import *

# data en dur à supprimer plus tard
data = {'name': "kais",
        'company': "efrei",
        'position': "dev",
        'email': 'kais.zeghdoud@efrei.net',
        'address': '0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5',
        'pk': '0x999999cf1046e68e36E1aA2E0E07105eDDD1f08E',
        'votes': 0}

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
@app.route('/VotinCorpo')
def index():
    return render_template('index.html')

# Connexion à Ganache
ganache_url = "http://127.0.0.1:7545"  # Mettez à jour avec l'URL de votre Ganache
web3 = Web3(Web3.HTTPProvider(ganache_url))   

contract_abi = [
			{
				"inputs": [
					{
						"internalType": "address",
						"name": "_voterAddress",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "_voteContractAddress",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "_fullName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "_company",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "_position",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "_email",
						"type": "string"
					}
				],
				"stateMutability": "nonpayable",
				"type": "constructor"
			},
			{
				"inputs": [],
				"name": "company",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "email",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "fullName",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "position",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "uint256",
						"name": "_candidateId",
						"type": "uint256"
					}
				],
				"name": "vote",
				"outputs": [],
				"stateMutability": "nonpayable",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "voteContractAddress",
				"outputs": [
					{
						"internalType": "address",
						"name": "",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "voterAddress",
				"outputs": [
					{
						"internalType": "address",
						"name": "",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "voterInfo",
				"outputs": [
					{
						"internalType": "string",
						"name": "",
						"type": "string"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "votesMade",
				"outputs": [
					{
						"internalType": "uint256",
						"name": "",
						"type": "uint256"
					}
				],
				"stateMutability": "view",
				"type": "function"
			}
		],

contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"

elector_contract = web3.eth.contract(address=contract_address, abi=contract_abi)


@app.route('/accounts')
def get_accounts():
    try:
        accounts = web3.eth.accounts
        return jsonify({'accounts': accounts}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        position = request.form['position']
        email = request.form['email']
        address = request.form['address']
        elector = (name, company, position, email, address)
        # appel fonction solidity : constructor of Elector
        tx_hash = elector_contract.constructor(
            address, 
            contract_address,
            name,
            company,
            position,
            email
        ).transact({'from': address})

        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        print("Transaction receipt:", receipt)
        print(elector)
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        address = request.form['address']
        pk = request.form['pk']
        accounts = get_accounts()
        if accounts:
            if address in accounts:
                if accounts[address] == pk:
                    return redirect('/MyElectorSpace')
                else:
                    flash("Invalid private key!")
            else:
                flash("Invalid Address...")
        else:
            flash("Blockchain unreachable, make sure that ganache is launched")

    return render_template('login.html')


@app.route('/MyElectorSpace', methods=['GET'])
def elector():
    return render_template('elector.html', user = data)


@app.route('/elections')
def elections():
    return render_template('elections.html')
