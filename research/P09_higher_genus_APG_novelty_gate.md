# P09 — Higher-genus APG: partition reduction and a necessary novelty condition
Date: 2026-10-24
Author: Mohammad Amir Khusru Akhtar
Status: rigorous no-go criterion, not a new string-theory breakthrough.

## Context
APG I and the Shannon–Rényi manuscript use power-sum deformations of normalized positive weights. P05–P08 investigated Narain momentum–winding energies, charge pairings and higher-genus information. Henriksson, Kakkar and McPeak (2023) already establish that some code CFTs with identical genus-one partition functions differ at genus two. The higher-genus distinction alone cannot be claimed as new.

## Theorem P09-T1: universal escort reduction
For any finite nonempty set S with real energies E_z and beta>0, define Z_S(beta)=sum_z exp(-beta E_z), p_z=exp(-beta E_z)/Z_S(beta), and D_(2q)=1-sum_z p_z^q, q>0. Then
D_(2q)=1-Z_S(q beta)/Z_S(beta)^q.
This identity holds regardless of whether S consists of Narain charges, higher-genus charge tuples, or any other finite configuration. It follows immediately by substitution. Therefore a proposed APG higher-genus invariant that merely applies this power sum to Gibbs weights is fully determined by the corresponding higher-genus theta/partition data.

## Corollary P09-C1: indistinguishability
If two models have identical Z_S(beta) for all beta>0 with matching finite-state conventions, they have identical D_(2q)(beta) for every beta,q>0. Hence escort power sums cannot recover interactions or geometric data absent from their input partition functions.

## Theorem P09-T2: finite-size sharp bound
For q>1 and N=|S|, 0<=D_(2q)<=1-N^(1-q), with upper equality exactly when all Gibbs weights are uniform; for N>1 and finite energies, the lower bound is strict. This is Jensen's inequality and is standard.

## What a genuine breakthrough would require
Construct a complete, physically admissible family of CFTs and an APG-derived observable not determined by their established partition, flavored partition, or higher-genus theta data. Prove modular/duality covariance, identify new information with an independent physical meaning, and demonstrate a sharp theorem beyond existing literature. No such construction has been demonstrated here.

## Decision
P09-T1 and P09-T2 are correct but classical. NO-GO on the claim that APG escort entropy of genus-two theta weights is novel. Do not state that string theory has been disproved or changed.
