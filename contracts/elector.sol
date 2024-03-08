// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Elector {
    // Adresse de l'électeur
    address public voterAddress;

    // Adresse du contrat de vote auquel l'électeur est associé
    address public voteContractAddress;

    // Indique si l'électeur a déjà voté
    bool public hasVoted;

    // Modificateur pour restreindre l'accès à certaines fonctions à l'électeur lui-même
    modifier onlyVoter() {
        require(msg.sender == voterAddress, "Only the voter can call this function");
        _;
    }

    // Constructeur du contrat
    constructor(address _voterAddress, address _voteContractAddress) {
        voterAddress = _voterAddress;
        voteContractAddress = _voteContractAddress;
    }

    // Fonction pour permettre à l'électeur de voter pour un candidat
    function vote(uint256 _candidateId) external onlyVoter {
        require(!hasVoted, "You have already voted");
        Vote(<voteContractAddress>).vote(_candidateId);
        hasVoted = true;
    }
}
