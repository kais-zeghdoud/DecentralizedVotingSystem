// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vote {

    // Adresse du propriétaire du contrat (probablement le conseil d'administration)
    address public owner;

    // Nombre total de votes
    uint256 public totalVotes;

    // Indique si les votes sont actuellement en cours
    bool public votingOpen;

    // Structure représentant un candidat et liste associée
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }
    Candidate[] public candidates;

    // Mapping pour enregistrer les votes des employés
    mapping(address => bool) public hasVoted;

    // Événement émis lorsqu'un vote est enregistré
    event Voted(address indexed voter, uint256 candidateId);

    // Modificateur pour restreindre l'accès à certaines fonctions au propriétaire du contrat
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modificateur pour restreindre l'accès à certaines fonctions tant que les votes sont ouverts
    modifier onlyDuringVoting() {
        require(votingOpen, "Voting is not currently open");
        _;
    }

    // Constructeur du contrat
    constructor() {
        owner = msg.sender;
        votingOpen = true;
    }

    // Fonction pour ajouter un candidat
    function addCandidate(string memory _name) external onlyOwner onlyDuringVoting {
        uint256 candidateId = candidates.length;
        candidates.push(Candidate(candidateId, _name, 0));
    }

    // Fonction pour permettre aux employés de voter pour un candidat
    function vote(uint256 _candidateId) external onlyDuringVoting {
        require(_candidateId < candidates.length, "Invalid candidate ID");
        require(!hasVoted[msg.sender], "You have already voted");
        
        candidates[_candidateId].voteCount++;
        totalVotes++;
        hasVoted[msg.sender] = true;

        emit Voted(msg.sender, _candidateId);
    }

    // Fonction pour fermer les votes
    function closeVoting() external onlyOwner onlyDuringVoting {
        votingOpen = false;
    }
}

