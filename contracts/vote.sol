// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vote {

    address public owner;
    uint256 public totalVotes;
    bool public votingOpen;

    struct Candidate {
        uint256 id;
        string name;
        uint256 voteCount;
    }
    Candidate[] public candidates;

    mapping(address => bool) public hasVoted;

    event Voted(address indexed voter, uint256 candidateId);
    // Événement pour le décompte des votes
    event VotesCounted(string name, uint256 voteCount);

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
        votingOpen = true;
    }

    function addCandidate(string memory _name) external onlyOwner onlyDuringVoting {
        candidates.push(Candidate(candidates.length, _name, 0));
    }

    function vote(uint256 _candidateId) external onlyDuringVoting {
        require(_candidateId < candidates.length, "Invalid candidate ID");
        require(!hasVoted[msg.sender], "You have already voted");
        
        candidates[_candidateId].voteCount++;
        totalVotes++;
        hasVoted[msg.sender] = true;

        emit Voted(msg.sender, _candidateId);
    }

    function closeVoting() external onlyOwner onlyDuringVoting {
        votingOpen = false;
        // Émet un événement avec le décompte des votes pour chaque candidat
        for(uint256 i = 0; i < candidates.length; i++) {
            emit VotesCounted(candidates[i].name, candidates[i].voteCount);
        }
    }
}


