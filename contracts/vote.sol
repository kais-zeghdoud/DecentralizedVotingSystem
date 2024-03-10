// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vote {

    address public owner;
    uint256 public totalVotes;
    bool public votingOpen;

    uint256 public currentRound = 0;
    mapping(address => uint256) public lastVotedRound;
    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }
    Candidate[] public candidates;

    mapping(address => bool) public hasVoted;

    event Voted(address indexed voter, uint256 candidateId);
    event VotesCounted(string name, uint256 voteCount);
    event VotingOpened();
    event VotingClosed();

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier onlyDuringVoting() {
        require(votingOpen, "Voting is not currently open");
        _;
    }

    constructor() {
        owner = msg.sender;
        votingOpen = false; // Démarre fermé pour permettre la configuration initiale
    }

    function addCandidate(string memory _name) external onlyOwner {
        require(votingOpen, "Cannot add candidate when voting is closed");
        candidates.push(Candidate(candidates.length, _name, 0));
    }

    function getCandidates() external view returns (Candidate[] memory) {
        return candidates;
    }
    
    function vote(uint256 _candidateId) external onlyDuringVoting {
        require(_candidateId < candidates.length, "Invalid candidate ID");
        require(lastVotedRound[msg.sender] < currentRound, "You have already voted in this round");
        
        candidates[_candidateId].voteCount++;
        totalVotes++;
        lastVotedRound[msg.sender] = currentRound; // Mise à jour du tour de vote pour cet électeur

        emit Voted(msg.sender, _candidateId);
    }

    function closeVoting() external onlyOwner onlyDuringVoting {
        votingOpen = false;
        for(uint256 i = 0; i < candidates.length; i++) {
            emit VotesCounted(candidates[i].name, candidates[i].voteCount);
        }
        emit VotingClosed();
    }

    function openVoting() external onlyOwner {
        require(!votingOpen, "Voting is already open");
        delete candidates; // Supprime tous les candidats précédents
        totalVotes = 0; // Réinitialise le compteur de votes total
        currentRound++; // Incrémente l'identifiant de tour pour réinitialiser le vote

        votingOpen = true;
        emit VotingOpened();
    }

}


