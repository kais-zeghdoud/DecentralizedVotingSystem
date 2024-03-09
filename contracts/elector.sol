// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVote {
    function vote(uint256 _candidateId) external;
}

contract Elector {
    address public voterAddress;
    address public voteContractAddress;
    bool public hasVoted;

    modifier onlyVoter() {
        require(msg.sender == voterAddress, "Only the voter can call this function");
        _;
    }

    constructor(address _voterAddress, address _voteContractAddress) {
        voterAddress = _voterAddress;
        voteContractAddress = _voteContractAddress;
    }

    function vote(uint256 _candidateId) external onlyVoter {
        require(!hasVoted, "You have already voted");
        IVote(voteContractAddress).vote(_candidateId);
        hasVoted = true;
    }
}

