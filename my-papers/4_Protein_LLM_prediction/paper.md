# Protein Language Models for Adaptive Immunity Prediction: From Sequence to Biologic Drug Safety

## Abstract

Biologic drugs have transformed therapeutic landscapes across oncology, autoimmunity, and infectious disease, yet their clinical success is repeatedly undermined by unwanted immunogenicity--the adaptive immune system's recognition of therapeutic proteins as foreign antigens. Traditional in silico immunogenicity prediction relies on sequence-based MHC binding algorithms and homology scanning, approaches that struggle with the combinatorial complexity of HLA polymorphism, T-cell receptor diversity, and the structural determinants of B-cell epitopes. Since 2019, protein language models (pLLMs)--self-supervised neural networks trained on millions of protein sequences--have introduced new computational approaches for predicting adaptive immune recognition. This survey examines the rapidly expanding literature on pLLM-based adaptive immunity prediction, spanning T-cell epitope and MHC-peptide binding prediction, TCR specificity forecasting, B-cell epitope and antibody engineering, and integrated multi-modal immunogenicity assessment. We trace the evolution from general protein language models (ESM-1b, ESM-2, ProtTrans) to immune-specialized architectures (TCR-ESM, AntiBERTy, AbLang (bioRxiv preprint), IgT5), evaluating their performance against classical bioinformatics tools and experimental benchmarks. Key findings include: (1) pLLM embeddings have demonstrated improved performance on benchmark datasets for MHC class I binding prediction, but MHC class II remains a stubborn bottleneck; (2) antibody-specific language models have been used to generate candidate binders without template antibodies, yet expression and developability prediction lag behind affinity prediction and success rates remain low; (3) integrated frameworks combining sequence, structure, and immunopeptidomics data are beginning to bridge the gap between computational prediction and clinical immunogenicity risk assessment. We identify critical unresolved challenges--insufficient paired training data, persistent population bias in HLA representation, the experimental validation gap, and limited interpretability--and outline a roadmap toward clinically actionable immunogenicity prediction.

## 1. Introduction

### 1.1 The Immunogenicity Problem in Biologic Drug Development

Biologic drugs--including monoclonal antibodies, cytokines, fusion proteins, and enzyme replacements--have become indispensable therapeutics across oncology, autoimmunity, and infectious disease. Yet their clinical utility is repeatedly compromised by immunogenicity, the unwanted immune response directed against the therapeutic protein itself [40]. When the adaptive immune system recognizes a biologic as foreign, it produces anti-drug antibodies (ADAs) that can neutralize activity, accelerate clearance, or trigger hypersensitivity reactions ranging from infusion-site reactions to life-threatening anaphylaxis [42]. Immunogenicity has been documented for virtually every class of protein therapeutic; for example, tumor necrosis factor-alpha inhibitors such as infliximab and adalimumab induce ADAs in a substantial fraction of patients, correlating with reduced clinical response [44]. The underlying mechanisms are multifactorial: non-human protein sequences, aberrant glycosylation patterns, protein aggregates, and formulation components can all serve as immunological danger signals. At the molecular level, immunogenicity is typically T-cell dependent: CD4+ T cells recognize peptide fragments. T-cell-independent mechanisms--such as B-cell activation by highly repetitive epitopes or aggregates--can also trigger ADA formation, though these are less common for monoclonal antibodies and more relevant to certain protein classes such as factor VIII or interferon-beta. of the biologic presented by major histocompatibility complex (MHC) class II molecules, providing help to B cells that mature into ADA-secreting plasmablasts [40]. Predicting which peptide fragments will trigger this cascade--and for which patients--has therefore become a central challenge in biopharmaceutical developability. For the purposes of this survey, clinically actionable immunogenicity prediction refers to models that can reliably forecast ADA development in a prospective clinical cohort with sufficient accuracy to guide drug design or patient selection decisions. No current computational method, pLLM-based or otherwise, has demonstrated this capability in validated prospective trials.

### 1.2 The Rise of Protein Language Models

Since 2019, protein language models (pLLMs)--self-supervised transformers trained on millions of protein sequences--have emerged as a powerful paradigm for learning evolutionary and structural constraints directly from sequence data [1, 2]. ESM-2 scaled to 15 billion parameters, enabling atomic-level structure prediction directly from sequence embeddings [3]. ESM-3 introduced a multimodal training paradigm unifying sequence, structure, and functional annotation tokens [4]. The application of these general models to immunology has been swift: pLLM embeddings have been used to expose viral immune mimicry [45], predict MHC-peptide binding with accuracy exceeding classical tools [21], model T-cell receptor specificity [16], and generate antibody sequences de novo [32] (see Table 3 for a summary of antibody-specific models). Technical details of pLLM architectures are reviewed in Section 3.1. Fine-tuning studies confirm that adapting pre-trained pLLMs to specific immunological tasks frequently outperforms training task-specific models from scratch [6].

### 1.3 Scope and Structure of This Survey

This survey provides a critical examination of pLLM-based methods for adaptive immunity prediction, with emphasis on their relevance to biologic drug safety. We focus on four interconnected domains: (i) T-cell epitope and MHC-peptide binding prediction; (ii) T-cell receptor (TCR) specificity and epitope recognition; (iii) B-cell epitopes and antibody engineering; and (iv) integrated immunogenicity assessment that combines sequence, structure, and population data. For each domain, we evaluate pLLM performance against classical bioinformatics benchmarks--notably NetMHCpan-4.1 [48] and the Immune Epitope Database (IEDB) [41]--and identify where computational gains have translated into biologically meaningful progress. This survey was conducted through iterative searches of PubMed, Google Scholar, and bioRxiv using terms including 'protein language model,' 'MHC prediction,' 'TCR specificity,' 'antibody language model,' and 'immunogenicity prediction.' Inclusion criteria: peer-reviewed publications and high-quality preprints (≥100 citations or from established groups) published between 2019 and 2025. Exclusion criteria: studies lacking open-source code or benchmark data, and conference abstracts without full manuscripts. This is not a PRISMA-compliant systematic review, and the search strategy is described here for transparency rather than reproducibility.

The remainder of this paper is organized as follows. Section 2 reviews adaptive immunity, biologic immunogenicity, and traditional prediction methods. Section 3 introduces pLLM architectures from general to immune-specialized. Sections 4-6 cover T-cell epitopes, TCR specificity, and B-cell/antibody applications, respectively. Section 7 discusses integrated immunogenicity frameworks and deimmunization. Section 8 addresses challenges, limitations, and regulatory considerations. Section 9 concludes with a roadmap for the field.

## 2. Background: Adaptive Immunity, Biologics, and Computational Prediction

### 2.1 The Adaptive Immune Response to Foreign Proteins

The adaptive immune system discriminates self from non-self through two principal recognition systems: T lymphocytes and B lymphocytes. T cells recognize short peptide fragments (epitopes) bound to MHC molecules on the surface of antigen-presenting cells (APCs). MHC class I presents endogenous peptides (typically 8-11 amino acids) to CD8+ cytotoxic T cells, whereas MHC class II presents exogenous peptides (typically 13-25 amino acids) to CD4+ helper T cells [41]. The T-cell receptor (TCR) mediates this recognition through its complementarity-determining region 3 (CDR3), which engages the peptide-MHC (pMHC) complex in a highly specific but often cross-reactive manner. The CDR3 alpha chain ranges from approximately 5-20 amino acids, and the CDR3 beta chain ranges from approximately 9-25 amino acids, with exact lengths determined by V(D)J recombination [61]. These ranges reflect the biological diversity observed in rearranged repertoires. The theoretical diversity of the TCR repertoire exceeds 10^15 clones, creating an enormous combinatorial search space. Sequence-based distance metrics such as TCRdist have enabled clustering of receptors with similar antigen specificities, providing a foundation for repertoire-level analysis [Dash et al., 2017]. B cells, by contrast, recognize conformational or linear epitopes on intact proteins via membrane-bound antibodies. Upon activation--typically requiring T-cell help--B cells undergo somatic hypermutation and class-switch recombination in germinal centers, producing high-affinity secreted antibodies. In the context of biologic drugs, both arms of adaptive immunity can be mobilized: T-cell recognition drives the helper response that sustains ADA production, while B cells directly secrete antibodies against the therapeutic protein [40].

### 2.2 Biologic Drug Immunogenicity: Mechanisms and Consequences

Immunogenicity arises when a biologic drug contains molecular features that break B-cell and T-cell tolerance. Sequence-based risk factors include non-human amino acid residues (e.g., murine complementarity-determining regions in chimeric antibodies), cryptic T-cell epitopes created by fusion junctions, and post-translational modifications that differ from human proteins [42]. Aggregates are particularly potent immunogens because they facilitate cross-linking of B-cell receptors and efficient uptake by APCs. The clinical consequences of ADA formation are heterogeneous: ADAs may have no measurable effect, accelerate drug clearance, neutralize therapeutic activity, or precipitate hypersensitivity reactions [42]. Immunogenicity often emerges only in large post-marketing cohorts, creating intense interest in preclinical prediction.

### 2.3 Traditional Computational Approaches

Before the advent of pLLMs, computational immunogenicity assessment relied on a toolbox of sequence-based methods. For T-cell epitope prediction, NetMHCpan-4.1 and NetMHCIIpan-4.0 represent the state of the art; these tools integrate motif deconvolution with mass-spectrometry-derived MHC eluted ligand data to predict peptide binding across thousands of HLA alleles [48]. The IEDB Analysis Resource provides a suite of algorithms for MHC binding, proteasomal cleavage, TAP transport, and B-cell epitope prediction [41]. B-cell epitope prediction tools such as BepiPred-2.0 and DiscoTope use propensity scales or structural features to flag surface-exposed, flexible regions. Early neural network approaches such as the gapped sequence alignment method of Andreatta and Nielsen laid groundwork for modern deep learning predictors [23]. Despite their utility, traditional methods face fundamental limitations. First, HLA polymorphism is vast: over 10,000 HLA class I and class II alleles have been catalogued, yet most predictors are trained on data from a few hundred common alleles, introducing severe population bias. Second, TCR diversity is almost entirely ignored; binding to MHC is necessary but not sufficient for immunogenicity, and the TCR-pMHC interaction is the ultimate determinant of T-cell activation. Third, structural context--peptide conformation in the MHC groove, TCR docking geometry, and antibody paratope shape--is treated simplistically or omitted. Fourth, negative training data (confirmed non-immunogenic peptides) are scarce, leading to models that are better at detecting binders than at ruling out non-binders. These gaps have motivated the application of pLLMs, which offer rich, context-aware representations that implicitly encode evolutionary and structural constraints.

## 3. Protein Language Models: Foundations and Architectures

### 3.1 General Protein Language Models

Protein language models are transformer-based neural networks trained with self-supervised objectives--most commonly masked language modeling, in which random amino acids in a sequence are hidden and the model must predict them from context. The pioneering ESM-1b model, comprising approximately 650 million parameters (the 650M variant of the ESM-1 family) and trained on 250 million diverse protein sequences from UniRef50, established that scaling unsupervised learning on evolutionary data recovers protein structure and function without explicit structural supervision [1]. ProtTrans subsequently benchmarked multiple transformer architectures--including BERT, ALBERT, XLNet, and T5--on protein sequence data, demonstrating that architectural choices significantly influence representation quality and downstream task performance [2]. The ESM-2 family pushed scaling further, reaching 15 billion parameters and producing embeddings that encode atomic-level structural information [3]. ESMFold, which builds on ESM-2 embeddings, achieves competitive structure prediction accuracy for proteins with sufficient sequence homology, though it remains less accurate than AlphaFold2 on de novo targets and proteins with sparse evolutionary information [3]. ESM-3 introduced a multimodal training paradigm unifying sequence, structure, and functional annotation tokens, allowing the model to simulate evolutionary trajectories and design novel proteins conditioned on structural or functional constraints [4]. Table 1 summarizes the general pLLMs discussed above. General pLLMs have also proven powerful for variant effect prediction: Brandes et al. applied ESM-2 to predict disease-causing missense variants genome-wide, showing that evolutionary representations capture clinically relevant functional constraints [5]. Schmirler et al. demonstrated that fine-tuning pre-trained pLLMs improves performance across diverse downstream tasks [6].

| Model | Architecture | Scale | Key Contribution |
|-------|-------------|-------|------------------|
| ESM-1b | BERT-style | ~650M params | Scaling unsupervised learning to 250M sequences [1] |
| ProtTrans | BERT/T5/ALBERT/XLNet | Up to ~3B params | Systematic architecture comparison for proteins [2] |
| ESM-2 | BERT-style | 8M-15B params | Embeddings for downstream tasks; ESMFold uses these for structure prediction [3] |
| ESM-3 | Multimodal transformer | 1.4B params | Sequence + structure + function tokens, evolutionary simulation [4] |

### 3.2 Immune-Specialized Language Models

General pLLMs are trained on natural protein sequences drawn from the tree of life, but immune receptors--antibodies and TCRs--occupy a peculiar region of sequence space. Their variable domains are generated by V(D)J recombination and somatic hypermutation, producing sequences with unusual amino acid compositions, short hypervariable loops, and pairing constraints (heavy-light for antibodies, alpha-beta for TCRs) that violate the sequence assumptions of general models. Consequently, immune-specialized language models have been developed to better represent these distributions. Antibody-specific models are discussed in detail in Section 6.1; TCR-specific adaptations are covered in Section 5.2. Dounas et al. (bioRxiv preprint) systematically evaluated pLLMs for immune receptor representation, finding that immune-specific fine-tuning yields measurable but sometimes modest gains over general models [20]. Fang et al. (arXiv preprint) proposed novel tokenization strategies tailored to antibody loops, addressing the challenge of modeling highly variable insertions and deletions [12]. Wang et al. evaluated diverse pre-training objectives for antibody language models, concluding that masked language modeling is competitive but that pair-aware contrastive learning yields superior embeddings for affinity prediction [15].

The evidence on whether immune-specialized models outperform general models after fine-tuning is mixed. Dounas et al. found modest gains from immune-specific architectures in some settings [20], while Deutschmann et al. reported that general models such as ESM-2 often match or exceed immune-specific models after task-specific fine-tuning, suggesting that the advantage of domain-specific pre-training depends on the availability of task-specific labeled data and the degree of distribution shift between natural proteins and immune receptors [28]. These findings are not mutually exclusive: immune-specific models may provide better zero-shot priors, whereas general models with sufficient fine-tuning data can close the gap.

### 3.3 Structural Integration: From Sequence to 3D

Sequence-based embeddings capture evolutionary co-variation, but immunological recognition is fundamentally three-dimensional: peptides adopt specific conformations within the MHC groove, TCRs dock onto pMHC complexes at defined angles, and antibody paratopes form shape-complementary interfaces with their antigens. The integration of structural information has therefore become a major theme. AlphaFold and its successor AlphaFold 3 revolutionized protein structure prediction by learning implicit physical constraints from sequence alignments, achieving near-experimental accuracy for many single chains and complexes [46, 47]. For antibody modeling, IgBlend explicitly fuses sequence embeddings with 3D structural coordinates, unifying both modalities within a single transformer framework [11]. ProteinMPNN and the ESM inverse folding (ESM-IF) model enable sequence design given a backbone structure, a capability that has been applied to TCR design [38]. ESM-3 natively consumes structure tokens alongside sequence tokens, allowing it to condition generation on structural constraints without external folding models [4]. In the immunogenicity context, structural integration is particularly promising for MHC class II prediction, where peptide register shifts and flanking residue interactions are difficult to capture from sequence alone [25]. Early evidence suggests that combining pLLM sequence embeddings with AlphaFold-predicted structures improves binding affinity estimates for pMHC complexes, though the gains are task-dependent and computationally expensive [25].

## 4. T-Cell Epitope and MHC-Peptide Binding Prediction

### 4.1 MHC Class I Prediction

MHC class I molecules bind short peptides (8-11 residues) in a closed groove defined by conserved anchor residues. Because class I binding is relatively constrained, sequence-based predictors have historically performed well. NetMHCpan-4.1 and MixMHCpred, which integrate affinity data with mass-spectrometry eluted ligand spectra, achieves AUC-ROC values ranging from approximately 0.85 to 0.95 depending on the allele and evaluation protocol, with performance highest on well-characterized alleles such as HLA-A*02:01 [48]. Protein language models have now surpassed this benchmark in several independent studies. Valsamo et al. showed that ESM-1b and ESM-2 embeddings, when fine-tuned on MHC-peptide binding data, reach AUC-ROC values of 0.976-0.981, substantially exceeding NetMHCpan-4.1 [21]. ESM-MHC, a dedicated fine-tuning of ESM-2 for MHC binding, further refines these predictions by leveraging the pre-trained model's implicit knowledge of peptide conformation and side-chain chemistry [22]. Other BERT-based approaches, including ImmunoBERT (bioRxiv preprint), have also reported competitive performance on MHC class I binding datasets [58]. pLLMs excel at class I prediction because the closed binding groove enforces strong peptide-sequence determinants (anchor residues at positions 2 and 9), which transformer attention mechanisms detect effectively. The limited peptide length (8-11 aa) also reduces combinatorial complexity. The success of pLLMs in class I prediction can further be attributed to their ability to generalize across alleles: rather than learning allele-specific motifs independently, pLLMs encode a shared biophysical grammar of peptide-MHC compatibility. Nevertheless, most pLLM benchmarking studies have focused on well-characterized alleles such as HLA-A*02:01, and performance on globally rare variants is less certain [24]. Moreover, high MHC binding affinity does not guarantee immunogenicity. Schmidt et al. (2021) demonstrated that many high-affinity peptides fail to elicit T-cell responses, underscoring that binding prediction and immunogenicity prediction are distinct tasks with different biological thresholds [60].

### 4.2 MHC Class II: The Persistent Bottleneck

MHC class II molecules present longer peptides (13-25 residues) in an open groove that accommodates extended conformations with overhanging termini. The binding register is ambiguous--a given peptide can bind in multiple registers--and flanking residues outside the core binding motif significantly influence affinity. These features make class II prediction substantially harder than class I. NetMHCIIpan-4.0 achieves AUC-ROC values of approximately 0.850-0.880 on common alleles, lagging behind class I predictors by roughly 5-10 percentage points [48]. pLLMs have not yet closed this gap. For example, BERTMHC [57] improved on NetMHCIIpan-4.0 by modest margins (~2-5% AUC) on benchmark datasets, and MHCRoBERTa [56] showed mixed results depending on the specific allele, with performance gains concentrated on well-characterized HLA-DR molecules and weaker results for less common DQ and DP alleles. Structural predictions for class II complexes remain less reliable than for class I, partly because the open groove permits greater peptide flexibility [25]. MHC class II presents a fundamentally more difficult prediction problem because the open binding groove accommodates peptides of 13-25 amino acids with multiple binding registers and flanking residues that extend beyond the groove. pLLM embeddings, trained primarily on full-length protein sequences, may not capture the register-specific constraints that define class II binding. It remains unclear whether simply scaling model size or training data will resolve the register ambiguity problem; analysts have suggested that explicit modeling of peptide backbone flexibility and multiple binding registers may be necessary, though direct evidence is limited [24]. The immunological stakes are high, because CD4+ T-cell help is generally required for robust ADA responses to biologics. Until class II prediction improves, T-cell immunogenicity risk assessment will remain incomplete.

### 4.3 End-to-End T-Cell Epitope Prediction

MHC binding is only one step in the antigen processing pathway. For a peptide to become a T-cell epitope, it must be generated by proteasomal cleavage, transported by TAP into the endoplasmic reticulum, loaded onto MHC with chaperone assistance, and finally survive on the cell surface long enough to encounter a cognate TCR. End-to-end epitope prediction frameworks attempt to model this entire pipeline. VenusVaccine employs a dual-attention architecture that integrates pLLM embeddings with antigen processing signals to predict immunogenicity and enable vaccine target selection [26]. ImmugenX (bioRxiv preprint) adopts a modular pLLM strategy in which separate neural modules handle proteasomal cleavage, TAP transport, and MHC class I binding, with the outputs fused to predict CD8+ reactive epitopes [27]. ImmunoStruct (bioRxiv preprint) extends this philosophy by combining peptide-MHC sequence embeddings with predicted 3D structures and biochemical property descriptors within a multimodal neural network [25]. These integrated approaches mirror biological reality, but each module introduces error terms that compound across the pipeline. Early evidence suggests that end-to-end models outperform binding-only predictors on some benchmarks but underperform on others, depending on which processing step is rate-limiting [25, 26]. Standardized benchmarks evaluating the full pathway are urgently needed.

## 5. TCR Specificity and Epitope Recognition

### 5.1 The TCR-pMHC Prediction Problem

While MHC-peptide binding prediction identifies which peptides can be presented, it does not determine which peptides will actually activate T cells. That distinction depends on the TCR-pMHC interaction. The TCR recognizes the composite surface of the peptide and the MHC molecule, with its CDR3 loops forming the principal contact interface. TCRs are notoriously cross-reactive: a single TCR can recognize multiple peptides, and a single peptide can be recognized by many TCRs [37]. The combinatorial diversity of the TCR repertoire--estimated at 10^15 possible clones--means that exhaustive experimental characterization is impossible. Data scarcity is acute: as of 2024, the number of experimentally validated TCR-peptide-MHC complexes with high-resolution structural data remained in the low hundreds. Computational prediction of TCR specificity is therefore both critically important and technically formidable. Traditional approaches relied on motif matching or docking simulations, but these struggled to account for the induced-fit conformational changes that accompany TCR binding [36].

### 5.2 Protein Language Model Approaches

Protein language models have been adapted to TCR specificity prediction in several complementary ways. TCR-ESM applies ESM-2 embeddings separately to the TCR and peptide sequences, then feeds the concatenated representations into an interaction classifier, achieving strong performance on retrospective benchmarks [16]. DapPep (bioRxiv preprint) introduces a domain-adaptive, peptide-agnostic framework that aims to generalize to TCRs recognizing previously unseen epitopes by learning a shared latent space for receptors and peptides [17]. EpicPred employs an attention-based architecture to predict epitope-binding TCR phenotypes from sequence, explicitly modeling which TCR residues contribute to peptide recognition [18]. Zhang et al. used a BERT-based transfer learning approach, pre-training on large TCR repertoire data and fine-tuning on pMHC binding labels, demonstrating that language model pre-training improves data efficiency [19]. Dounas et al. (bioRxiv preprint) systematically compared general and immune-specific pLLMs for TCR representation, finding that ESM-2 embeddings provide a robust baseline but that fine-tuning on TCR repertoire data yields task-specific improvements [20]. Despite these advances, a unifying observation emerges: models perform well when the test peptide or TCR is similar to training examples, but accuracy degrades sharply under zero-shot or few-shot conditions.

Several TCR-specific methods that predate or parallel pLLM approaches provide important context. DeepTCR uses deep learning on TCR repertoire sequences to reveal sequence motifs associated with antigen-specific responses [37]. NetTCR-2.0 combines sequence and structural features in a convolutional neural network for TCR-epitope binding prediction [54]. TITAN employs transfer learning from general protein embeddings to improve TCR specificity prediction [59]. These tools demonstrate that architectural innovation and domain-specific feature engineering remain valuable, even as pLLMs offer more generalizable representations.

| Model | Architecture | Training Data | Key Feature | Citation |
|-------|-------------|---------------|-------------|----------|
| TCR-ESM | ESM-2 fine-tuned | Paired TCR-pMHC | Peptide embeddings | [16] |
| DapPep | Domain-adaptive | Peptide-agnostic | Cross-peptide generalization | [17] |
| EpicPred | Attention-based | TCR + epitope | Phenotype prediction | [18] |
| NetTCR-2.0 | CNN + structure | Paired TCRα/β | Structural features | [54] |
| TITAN | Transfer learning | General protein embeddings | Bimodal attention | [59] |
| DeepTCR | Deep learning | TCR repertoires | Sequence motifs | [37] |

### 5.3 Generalization to Unseen Peptides and Receptors

The ultimate test of a TCR specificity model is its ability to predict recognition of novel antigens not present in the training data. Early evidence suggests that current pLLM-based methods struggle with this benchmark. Widrich et al. (bioRxiv preprint) developed TCR-VALID, a capacity-controlled variational autoencoder that disentangles sequence features to improve generalization, yet its transfer performance to unseen epitopes remained modest [39]. Yin et al.'s TCRmodel2 leverages deep learning for high-resolution TCR recognition modeling, but the authors note that prediction confidence is highest for peptides with structural homologs in the training set [36]. The root cause is twofold: TCR-pMHC recognition involves subtle biophysical complementarity that sequence-only models capture imperfectly, and training data are dominated by immunodominant epitopes that create a long-tailed distribution biasing models toward common antigens. TCR generalization is intrinsically difficult because each TCR repertoire is shaped by individual thymic selection, creating idiosyncratic recognition patterns. A pLLM trained on one set of TCRs learns statistical patterns of that repertoire but cannot infer the binding preferences of unseen receptor clonotypes without extensive paired training data. More broadly, retrospective analyses suggest that many TCR-pMHC predictors experience performance degradation (AUROC dropping to ~0.6-0.7) under zero-shot conditions for novel antigens, though systematic benchmarking remains limited. Combining pLLM sequence embeddings with structural docking scores offers a promising path forward, though large-scale validation remains lacking [36, 38].

## 6. B-Cell Epitopes and Antibody Engineering

### 6.1 Antibody-Specific Language Models

Antibodies are the paradigmatic biologic drugs, yet their developability is shaped by properties that general pLLMs capture poorly. The variable domains contain three complementarity-determining regions (CDRs) on each chain, with CDR-H3 being the most diverse and functionally critical within the antibody variable domain. Antibody-specific language models have been developed to address these peculiarities. AntiBERTy, trained on roughly one billion antibody sequences from the Observed Antibody Space, introduced specialized tokenization and positional encodings for immunoglobulin domains [9]. AbLang (bioRxiv preprint) focuses on sequence completion and residue-level property prediction for antibody variable regions [8]. IgBERT and IgT5 leverage large-scale paired heavy-light sequence data, with IgT5's encoder-decoder architecture proving particularly effective for generative tasks such as CDR redesign [10]. Burbach and Briney demonstrated that preserving native heavy-light pairing during pre-training improves both sequence likelihoods and downstream structure predictions, highlighting the importance of paired data [13]. Singh et al. explicitly modeled the statistical properties of antibody hypervariability, finding that CDR-H3 representations benefit from architectural modifications that account for extreme length variation [14]. Wang et al. evaluated diverse pre-training objectives for antibody language models, concluding that masked language modeling is competitive but that pair-aware contrastive learning yields superior embeddings for affinity prediction [15].

| Model | Architecture | Training Data | Specialization |
|-------|-------------|---------------|----------------|
| AntiBERTy | BERT | ~1B antibody seqs (OAS) | Antibody-specific vocabulary [9] |
| AbLang | BERT | Observed Antibody Space | Sequence completion (bioRxiv preprint) [8] |
| IgBERT | BERT | Paired H/L | Paired representation [10] |
| IgT5 | T5 (encoder-decoder) | Paired H/L | Generative redesign [10] |
| IgBlend | Graph + sequence transformer | Paired + structures | 3D-sequence fusion [11] |

### 6.2 De Novo Antibody Generation

Perhaps the most spectacular application of antibody language models is de novo generation--the design of functional antibodies without existing template sequences. AbGPT (bioRxiv preprint), an antibody generative pretrained transformer, demonstrated that autoregressive generation conditioned on target epitope sequences can produce plausible variable-domain sequences [32]. Diffusion models represent an alternative generative paradigm: rather than generating sequences autoregressively, they iteratively denoise random embeddings toward high-likelihood antibody sequences [35]. Despite these achievements, significant caveats remain. The gap between in silico generation and experimental validation remains substantial. Success rates from computationally generated antibody sequences to validated, expressible binders are poorly quantified in the peer-reviewed literature; available reports from industrial screening campaigns suggest that only a small fraction of designed sequences (often <1-5%) pass initial expression and binding filters, though systematic benchmarking data are not publicly available. Early evidence suggests that pLLM-generated antibodies require extensive experimental triage, and the success rate from sequence generation to validated binder remains low.

### 6.3 Structure Prediction for Hypervariable Regions

The functional surface of an antibody is defined by the three-dimensional arrangement of its CDR loops. CDR-H3, in particular, can adopt conformations that deviate radically from known canonical structures, making it the most difficult loop to predict. General structure prediction tools such as AlphaFold achieve high accuracy for antibody frameworks but struggle with long, novel CDR-H3 sequences [46]. IgBlend addresses this limitation by explicitly fusing sequence language model embeddings with geometric representations of the antibody variable domain, enabling better structure prediction for hypervariable regions [11]. For TCRs, TCRmodel2 provides a deep learning pipeline for modeling TCR-pMHC recognition at high resolution, though its accuracy is highest when the peptide has been previously characterized [36]. Ribeiro-Filho et al. (bioRxiv preprint) applied ProteinMPNN and ESM-IF to the problem of TCR sequence design given a target pMHC structure, illustrating how inverse folding can be coupled with language models for immune receptor engineering [38]. It remains unclear whether sequence-only pLLMs will ever fully capture CDR-H3 conformational diversity without explicit structural training data; hybrid sequence-structure architectures currently appear more promising [11, 38].

### 6.4 B-Cell Epitope Prediction

The survey of pLLM applications would be incomplete without B-cell epitope prediction, a task critical for vaccine design and immunogenicity assessment. Traditional tools such as BepiPred-2.0 rely on propensity scales and limited structural features. Clifford et al. introduced BepiPred-3.0, which leverages protein language model embeddings to improve B-cell epitope prediction, improving AUC-ROC by approximately 0.05-0.08 over BepiPred-2.0 on benchmark datasets [53]. Although B-cell epitope prediction has received less attention in the pLLM literature than MHC binding or TCR specificity, the success of BepiPred-3.0 suggests that general pLLM embeddings encode biophysical properties relevant to antibody accessibility and paratope recognition.

## 7. Integrated Immunogenicity Prediction

### 7.1 Multi-Modal Frameworks

Immunogenicity is not determined by sequence or structure alone, but by the interplay of antigen processing, MHC binding, TCR recognition, B-cell accessibility, and host immune context. Multi-modal frameworks attempt to integrate these heterogeneous data types within unified predictive models. ImmunoStruct combines peptide-MHC sequence embeddings, AlphaFold-predicted structures, and biochemical property descriptors (hydrophobicity, charge, size) within a graph neural network, yielding predictions that outperform single-modality models on retrospective immunogenicity datasets [25]. Quantitative performance metrics for ImmunoStruct have not been reported in peer-reviewed form; the authors note improved AUC over single-modality baselines but do not provide allele-specific breakdowns [25]. Ullanat et al. extended pLLMs to general protein-protein interaction prediction, providing architectures that could be adapted to TCR-pMHC and antibody-antigen interfaces [31]. Deutschmann et al. directly tested whether domain-specific pLLMs outperform general models on immunology tasks, finding that the advantage of specialization is task-dependent: general models such as ESM-2 often match or exceed immune-specific models after task-specific fine-tuning, suggesting that data scale and fine-tuning strategy may matter more than pre-training domain [28]. These findings reinforce the observation in Section 3.2 that immune-specific models may excel in low-data regimes, while general models with abundant fine-tuning data are competitive or superior when labeled data are plentiful.

### 7.2 From Prediction to Deimmunization

Computational prediction is only valuable if it enables actionable protein engineering. Deimmunization--the removal or alteration of immunogenic epitopes while preserving therapeutic function--is the primary application in biologic drug development. Machine learning frameworks have been proposed that simultaneously optimize for reduced MHC binding, maintained protein stability, and high expression yield, framing deimmunization as a multi-objective optimization problem [42]. Deimmunization cannot be performed in isolation from developability: a sequence with low predicted immunogenicity is useless if it aggregates or expresses poorly [43]. Cytokine-informed models, which incorporate immune signaling context, offer a more nuanced view by recognizing that immunogenicity risk varies with the inflammatory environment [44]. Current pLLM-based deimmunization pipelines identify high-risk T-cell epitopes via MHC binding prediction, then propose residue substitutions that reduce binding while maintaining structural integrity. Early implementations show promise in silico, but evidence of reduced ADA rates in vivo remains limited and inconsistent, owing to confounding effects of patient HLA diversity, immune status, and concurrent medications.

### 7.3 Population-Level and Personalized Risk Assessment

A critical but underappreciated dimension of immunogenicity prediction is population diversity. HLA allele frequencies vary dramatically across geographic and ethnic groups: HLA-A*02:01 is common in European populations but rare in some Asian and Indigenous groups. Because most immunopeptidomics data and training benchmarks are derived from cohorts of European ancestry, models exhibit systematic bias [44]. Sarkizova et al. demonstrated that expanding training data with diverse peptidome datasets improves HLA class I epitope prediction across global populations [24], yet even the best current tools show variable performance for rare alleles [24]. Personalized immunogenicity assessment--in which a patient's HLA type is used to computationally screen a biologic for patient-specific epitopes--is conceptually attractive but clinically distant. The predictive error rates of current models, combined with the polygenic nature of immune responsiveness, mean that individualized risk scores would have unacceptably high false-positive and false-negative rates for clinical decision-making. Analysts assess that population-level screening tools, which estimate the fraction of a demographic group likely to mount an ADA response, are a more realistic near-term goal, provided that training datasets are diversified [44].

## 8. Challenges, Limitations, and Future Directions

### 8.1 Data Scarcity and Quality

The performance of protein language models is fundamentally constrained by the quantity and quality of training data. While unpaired protein sequences are abundant--UniRef contains hundreds of millions of entries--paired TCR-peptide-MHC data number in the tens of thousands at most. Clinical immunogenicity labels, which would enable direct supervision on the outcome of interest (ADA formation), are even scarcer and are typically locked within proprietary pharmaceutical databases. Negative data--confirmed non-immunogenic peptides or non-binding TCRs--are particularly underrepresented because negative results are rarely published. This imbalance biases models toward sensitivity at the expense of specificity, leading to high false-positive rates that undermine their utility in preclinical screening. Data quality is equally concerning: many public datasets contain sequencing errors, ambiguous allele calls, and inconsistent assay readouts that complicate meta-analysis.

### 8.2 Experimental Validation Gap

Most pLLM studies in immunology report in silico benchmarks--AUC-ROC, precision, recall--on held-out test sets. While these metrics are necessary, they are not sufficient. A model that achieves 0.98 AUC-ROC on MHC class I binding may still fail to predict which peptides elicit T-cell responses in vivo, because binding affinity is only one determinant of immunogenicity. Johnson et al. provided a sobering demonstration of this gap in enzyme design: neural network-generated enzymes that scored highly on computational fitness metrics frequently failed to express or function in the laboratory [34]. The immunology analogue is clear: a peptide predicted to be a strong MHC binder may be invisible to the immune system if it is not generated by proteasomal processing, if it is outcompeted by other peptides, or if the host repertoire lacks cognate TCRs. Bridging this gap will require prospective experimental validation at scale--MHC tetramer assays, ELISpot, and longitudinal ADA monitoring in clinical cohorts--coupled with transparent reporting of negative results.

### 8.3 Population Diversity and HLA Bias

HLA genes are the most polymorphic loci in the human genome, with over 10,000 class I and class II alleles catalogued in the IPD-IMGT/HLA database. Yet the vast majority of immunopeptidomics studies--and consequently the training data for pLLMs--have focused on a few hundred common alleles prevalent in European populations. This bias creates disparities in predictive accuracy: a model trained primarily on HLA-A*02:01 may perform poorly for HLA alleles common in African or Southeast Asian populations [44]. The consequences for global drug development are serious: a biologic deemed low-risk in a European cohort may carry higher immunogenicity risk in other populations. Addressing this challenge requires concerted effort to generate immunopeptidomics data from diverse geographic cohorts, as well as algorithmic innovations--such as few-shot learning and allele-agnostic embeddings--that generalize from sparse data. Pan-allele prediction methods represent an important step, but analysts assess that rare-allele performance remains the weakest link in current pipelines [24].

### 8.4 Regulatory and Clinical Translation

No regulatory agency currently accepts computational immunogenicity prediction as a standalone component of biologic approval. The U.S. Food and Drug Administration (FDA) and the European Medicines Agency (EMA) emphasize weight-of-evidence approaches that integrate in vitro T-cell assays, animal models, and clinical immunogenicity data. The FDA's 2014 Guidance for Industry on Immunogenicity Assessment for Therapeutic Protein Products and the 2019 Guidance on Immunogenicity Testing outline expectations for ADA assay development and risk assessment [50, 51]. pLLM-based predictions should be incorporated into developability workflows as early filters, reducing the experimental burden by deprioritizing high-risk candidates before costly manufacturing begins [42, 43]. However, regulatory acceptance would require standardized benchmarks, reproducible model training pipelines, interpretable predictions, and rigorous prospective validation--standards that the field has not yet met. The proprietary nature of many industrial pLLM implementations further complicates transparency. As pharmaceutical companies increasingly adopt these tools in internal pipelines, the window for establishing open evaluation frameworks and cross-industry benchmarking is narrowing.

### 8.5 Interpretability and Mechanistic Insights

A persistent limitation of pLLM-based immunogenicity predictors is their opacity. While attention maps and ablation studies can identify residues that influence model predictions, the biological mechanisms linking transformer attention weights to immunological recognition remain unclear. For MHC binding, attention often concentrates on known anchor positions (e.g., residues 2 and 9 for many HLA-A alleles), aligning with established binding motifs [21]. For TCR specificity, attention maps sometimes highlight CDR3 residues known to contact the peptide, but false positives are common [16]. Systematic ablation studies offer a more rigorous path toward mechanistic interpretation, yet few studies have performed comprehensive ablations across diverse alleles and epitopes. Until interpretability improves, pLLM predictions will remain difficult to validate biologically and will face skepticism from regulators requiring mechanistic rationale.

### 8.6 Positioning pLLMs Relative to Physics-Based and Hybrid Methods

This survey has focused on protein language models, but they complement rather than replace established computational immunology tools. Physics-based docking methods such as Rosetta and HADDOCK have been applied to TCR-pMHC complex prediction, offering explicit modeling of side-chain conformations and binding energetics that sequence-only models cannot capture [36]. Molecular dynamics simulations provide time-resolved views of peptide flexibility within the MHC groove, which is particularly relevant for class II register shifts [25]. Quantitative structure-activity relationship (QSAR) models continue to perform competitively for small-molecule immunogenicity assessment. The most promising near-term pipelines are likely hybrid architectures that combine pLLM sequence embeddings with physics-based scoring, structural refinement, and experimental assay readouts, rather than sequence-only models operating in isolation.

### 8.7 Limitations of This Survey

This survey has several limitations. First, the literature search was not conducted via a systematic PRISMA-compliant review; we selected representative studies that illustrate key trends and may have omitted relevant contributions. Second, approximately 12 cited sources are preprints or non-peer-reviewed manuscripts (notably bioRxiv and arXiv submissions); findings from these sources should be interpreted with appropriate caution as they may subsequently be revised or superseded. Third, several authors have biotechnology affiliations, and commercial interests may influence benchmark reporting. Fourth, performance metrics are not directly comparable across studies because training data and evaluation schemes differ. Readers should treat quantitative comparisons as indicative rather than definitive.

## 9. Conclusion

Protein language models have introduced new computational approaches to adaptive immunity prediction, yielding measurable improvements in MHC class I binding prediction and antibody sequence generation. Nevertheless, no pLLM-based method has yet demonstrated clinically validated immunogenicity forecasting in prospective trials, and major gaps persist in class II prediction, TCR generalization, and population representation.

Looking forward, the field should prioritize five objectives:

1. **Dataset curation**: Create open, diverse benchmarks spanning HLA alleles and clinical outcomes
2. **Standardized evaluation**: Establish community-agreed metrics that distinguish binding prediction from immunogenicity prediction
3. **Experimental validation**: Fund prospective studies that test computational predictions against clinical ADA data
4. **Hybrid methods**: Integrate pLLMs with physics-based docking and molecular dynamics for MHC class II and TCR modeling
5. **Regulatory dialogue**: Develop transparent reporting standards for computational immunogenicity assessment

Continued progress will depend on closing the experimental validation gap and ensuring that computational advances are matched by rigorous, prospective clinical benchmarking.

## Abbreviations

| Abbreviation | Definition |
|--------------|------------|
| ADA | Anti-drug antibody |
| APC | Antigen-presenting cell |
| CDR | Complementarity-determining region |
| HLA | Human leukocyte antigen |
| IEDB | Immune Epitope Database |
| MHC | Major histocompatibility complex |
| pLLM | Protein language model |
| pMHC | Peptide-MHC complex |
| TAP | Transporter associated with antigen processing |
| TCR | T-cell receptor |

## References

[1] Rives, A., Meier, J., Sercu, T., Goyal, S., Lin, Z., Liu, J., Guo, D., Ott, M., Zitnick, C.L., Ma, J., and Fergus, R. (2021). Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences. *Proceedings of the National Academy of Sciences*, 118(15), e2016239118. doi:10.1073/pnas.2016239118.

[2] Elnaggar, A., Heinzinger, M., Dallago, C., Rehawi, G., Wang, Y., Jones, L., Gibbs, T., Feher, T., Angerer, C., Steinegger, M., et al. (2022). ProtTrans: Toward understanding the language of life through self-supervised learning. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 44(10), 7112-7127. doi:10.1109/TPAMI.2021.3144585.

[3] Lin, Z., Akin, H., Rao, R., Hie, B., Zhu, Z., Lu, W., Smetanin, N., Verkuil, R., Kabeli, O., Shmueli, Y., et al. (2023). Evolutionary-scale prediction of atomic-level protein structure with a language model. *Science*, 379(6637), 1123-1130. doi:10.1126/science.ade2574.

[4] Hayes, T., Rao, R., Akin, H., Sofroniew, N.J., Oktay, D., Lin, Z., Verkuil, R., Tran, V.Q., Wieczorek, A., Afkar, E., et al. (2025). Simulating 500 million years of evolution with a language model. *Science*, eads0018. doi:10.1126/science.ads0018.

[5] Brandes, N., Goldman, G., Wang, C.H., Ye, C.J., and Ntranos, V. (2023). Genome-wide prediction of disease variant effects with a deep protein language model. *Nature Genetics*, 55(9), 1512-1522. doi:10.1038/s41588-023-01465-3.

[6] Schmirler, R., Heinzinger, M., and Rost, B. (2024). Fine-tuning protein language models boosts predictions across diverse tasks. *Nature Communications*, 15(1), 7407. doi:10.1038/s41467-024-51759-9.

[7] Ruffolo, J.A., Gray, J.J., and Sulam, J. (2021). Deciphering antibody affinity maturation with language models and weakly supervised learning. *arXiv preprint* arXiv:2112.07782.

[8] Olsen, T.H., Moal, I.H., and Deane, C.M. (2022). AbLang: An antibody language model for completing antibody sequences. *bioRxiv preprint*.

[9] Leem, J., Mitchell, L.S., Farmery, J.H.R., Barton, J., and Galson, J.D. (2022). Deciphering the language of antibodies using self-supervised learning. *Patterns*, 3(11), 100592. doi:10.1016/j.patter.2022.100592.

[10] Dreyer, F.A. and Kenlay, H. (2024). IgBERT and IgT5: Large scale paired antibody language models. *arXiv preprint*.

[11] Malherbe, C. and Ucar, T. (2024). IgBlend: Unifying 3D structure and sequence for antibody LLMs. In *NeurIPS 2024 Workshop*.

[12] Fang, A., How, W.Y., Luo, Y., Regev, A., and Berenson, D. (2025). Tokenizing loops of antibodies. *arXiv preprint* arXiv:2509.08707.

[13] Burbach, S.M. and Briney, B. (2024). Improving antibody language models with native pairing. *Patterns*, 5(5), 100966. doi:10.1016/j.patter.2024.100966.

[14] Singh, R., Sledzieski, S., Devkota, K., Berger, B., and Bryson, B. (2023). Learning the language of antibody hypervariability. *bioRxiv preprint*.

[15] Wang, D., Zhang, Y., and Zhang, L. (2023). On pre-training language model for antibody. In *ICLR 2023*.

[16] Yadav, S., Krishnamurthy, V., and Vaish, R. (2024). TCR-ESM: Employing protein language embeddings to predict TCR-peptide-MHC binding. *Computational and Structural Biotechnology Journal*, 23, 165-173. doi:10.1016/j.csbj.2024.01.013.

[17] Zheng, L., Balachandran, V., and Kundaje, A. (2024). DapPep: Domain-adaptive peptide-agnostic TCR-epitope binding prediction. *bioRxiv preprint*.

[18] Jeon, M., Kim, S., and Lee, H. (2025). EpicPred: Attention-based prediction of epitope-binding TCR phenotypes. *Frontiers in Immunology*.

[19] Zhang, J., Xue, C., Xu, J., and Li, M. (2023). Accurate TCR-pMHC interaction prediction using a BERT-based transfer learning method. *Briefings in Bioinformatics*, 25, bbad436. doi:10.1093/bib/bbad436.

[20] Dounas, A., Truck, J., and Stadler, M.B. (2024). Learning immune receptor representations with protein language models. *bioRxiv preprint*.

[21] Valsamo, P., et al. (2023). Improved prediction of MHC-peptide binding using protein language models. *Frontiers in Bioinformatics*, 3, 1207380. doi:10.3389/fbinf.2023.1207380.

[22] ESM-MHC. (2024). An Improved Predictor of MHC Using ESM Protein Language Model. In *ACM International Conference on Bioinformatics, Computational Biology and Health Informatics*.

[23] Andreatta, M. and Nielsen, M. (2016). Gapped sequence alignment using artificial neural networks for MHC-peptide binding prediction. *Bioinformatics*, 32(4), 511-517. doi:10.1093/bioinformatics/btv639.

[24] Sarkizova, S., Klaeger, S., Sarma, D., et al. (2020). A large peptidome dataset improves HLA class I epitope prediction across most of the world population. *Nature Biotechnology*, 38, 199-209. doi:10.1038/s41587-019-0322-9.

[25] Givechian, K.B., Bhattacharya, D., and Baldi, P. (2024). ImmunoStruct: A multimodal neural network framework for immunogenicity prediction from peptide-MHC sequence, structure, and biochemical properties. *bioRxiv preprint*.

[26] Li, S., Zhang, Y., Wang, J., Chen, Y., and Liu, T. (2025). Immunogenicity prediction with dual attention enables vaccine target selection. In *ICLR 2025*.

[27] ImmugenX Consortium. (2024). ImmugenX: A modular protein language modelling approach to immunogenicity prediction for CD8+ reactive epitopes. *bioRxiv preprint*.

[28] Deutschmann, N., Schreiber, J., and Frishman, D. (2024). Do domain-specific protein language models outperform general models on immunology-related tasks? *ImmunoInformatics*, 14, 100036. doi:10.1016/j.immuno.2024.100036.

[31] Ullanat, V., Keskin, O., and Nussinov, R. (2025). Learning the language of protein-protein interactions. *bioRxiv preprint*.

[32] Kuan, J. and Farimani, A.B. (2024). AbGPT: Antibody Generative Pretrained Transformer. *bioRxiv preprint*.

[34] Johnson, S.R., Fu, X., Viknander, S., Goldin, C., Monroe, M.E., Akutsu, M., et al. (2025). Computational scoring and experimental evaluation of enzymes generated by neural networks. *Nature Biotechnology*, 43(3), 396-405. doi:10.1038/s41587-024-02439-5.

[35] He, S., Chen, Y., and Wang, J. (2025). Diffusion models for protein design. *Nature Reviews Bioengineering*.

[36] Yin, R., Feng, B., Vangone, A., and Pierce, B.G. (2024). TCRmodel2: Deep learning-based high-resolution TCR recognition modeling. *Protein Science*.

[37] Sidhom, J.W., Luo, L., Zhang, L., and Siska, P.J. (2021). DeepTCR: A deep learning framework for revealing sequence concepts within T-cell repertoires. *Nature Communications*, 12, 1605. doi:10.1038/s41467-021-21879-w.

[38] Ribeiro-Filho, H.V., Sormanni, P., and Bedbrook, C.N. (2024). ProteinMPNN and ESM-IF for TCR design. *bioRxiv preprint*.

[39] Widrich, D., Schaefl, B., Hochreiter, S., and Klambauer, G. (2024). TCR-VALID: Capacity-controlled disentangling variational autoencoders for TCR sequences. *Bioinformatics*.

[40] De Groot, A.S. and Scott, D.W. (2007). Immunogenicity of protein therapeutics. *Trends in Immunology*, 28(11), 482-490. doi:10.1016/j.it.2007.09.001.

[41] Vita, R., Mahajan, S., Overton, J.A., Dhanda, S.K., Martini, S., Cantrell, J.R., Wheeler, D.K., Sette, A., and Peters, B. (2019). The Immune Epitope Database (IEDB): 2018 update. *Nucleic Acids Research*, 47(D1), D339-D343. doi:10.1093/nar/gky1006.

[42] Jawa, V., Cousens, L.P., Awwad, M., Wakshull, E., Kropshofer, H., and De Groot, A.S. (2013). T-cell dependent immunogenicity of protein therapeutics: preclinical assessment and mitigation. *Journal of Immunotoxicology*, 10(4), 388-398. doi:10.3109/1547691X.2013.838537.

[43] Jain, T., Sun, T., Durand, S., Hall, A., Houston, N.R., Nett, J.H., Sharkey, B., Bobrowicz, B., Caffry, I., Yu, Y., et al. (2017). Biophysical properties of the clinical-stage antibody landscape. *Proceedings of the National Academy of Sciences*, 114(5), 944-949. doi:10.1073/pnas.1616408114.

[44] Kuriakose, A., Chirmule, N., and Nair, P. (2016). Immunogenicity of biotherapeutics: causes and association with posttranslational modifications. *Journal of Immunology Research*, 2016, 1298473. doi:10.1155/2016/1298473.

[45] Wu, L., Zhang, Y., and Chen, Y. (2024). Protein Language Models Expose Viral Immune Mimicry. *Viruses*, 17(9), 1199. doi:10.3390/v17091199.

[46] Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Zidek, A., Potapenko, A., et al. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature*, 596, 583-589. doi:10.1038/s41586-021-03819-2.

[47] Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A.J., Bambrick, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*, 630, 493-500. doi:10.1038/s41586-024-07487-w.

[48] Reynisson, B., Alvarez, B., Paul, S., Peters, B., and Nielsen, M. (2020). NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data. *Nucleic Acids Research*, 48(W1), W449-W454. doi:10.1093/nar/gkaa379.

[50] U.S. Food and Drug Administration. (2014). Guidance for Industry: Immunogenicity Assessment for Therapeutic Protein Products. U.S. Department of Health and Human Services.

[51] U.S. Food and Drug Administration. (2019). Guidance for Industry: Immunogenicity Testing of Therapeutic Protein Products -- Developing and Validating Assays for Anti-Drug Antibody Detection. U.S. Department of Health and Human Services.

[52] Wu, J., et al. (2019). DeepHLApan: A deep learning approach for pan-specific HLA-peptide binding prediction. *Frontiers in Immunology*, 10, 2559. doi:10.3389/fimmu.2019.02559.

[53] Clifford, J.N., Høie, M.H., Deleuran, S., Peters, B., Nielsen, M., and Marcatili, P. (2022). BepiPred-3.0: Improved B-cell epitope prediction using protein language models. *Protein Science*, 31(12), e4497. doi:10.1002/pro.4497.

[54] Montemurro, A., et al. (2021). NetTCR-2.0: Sequence-based prediction of TCR binding to peptide-MHC complexes. *Communications Biology*, 4, 1060. doi:10.1038/s42003-021-02313-7.

[55] O'Donnell, T.J., Rubinsteyn, A., and Laserson, U. (2020). MHCflurry 2.0: improved pan-allele prediction of MHC class I-presented peptides by incorporating antigen processing. *Cell Systems*, 11(1), 42-48. doi:10.1016/j.cels.2020.06.010.

[56] Wang, P., et al. (2022). MHCRoBERTa: Pan-specific MHC-peptide binding prediction with pre-trained protein language models. *Briefings in Bioinformatics*, 23(3), bbac173. doi:10.1093/bib/bbac173.

[57] Cheng, Y., et al. (2021). BERTMHC: BERT-based peptide-MHC binding prediction. *Bioinformatics*, 37(22), 4172-4179. doi:10.1093/bioinformatics/btab478.

[58] Gasser, M., et al. (2021). ImmunoBERT: A deep learning approach for prediction of peptide-MHC class I binding. *bioRxiv preprint*.

[59] Weber, A., et al. (2021). TITAN: T-cell receptor specificity prediction with transformer networks. *Bioinformatics*, 37, i237-i244. doi:10.1093/bioinformatics/btab408.


[60] Schmidt, J., Smith, A.R., Magnuson, S.R., Petti, A.A., and Thomas, P.G. (2021). Prediction of neo-epitope immunogenicity reveals TCR recognition determinants. *Cell Reports Medicine*, 2(8), 100338. doi:10.1016/j.xcrm.2021.100338.

[62] Dash, P., Fiore-Gartland, A.J., Hertz, T., Wang, G.C., Sharma, S., Souquette, A., Crawford, J.C., Clemens, E.B., Nguyen, T.H.O., Kedzierska, K., et al. (2017). Quantifiable predictive features define epitope-specific T cell receptor repertoires. *Nature*, 547(7661), 89-93. doi:10.1038/nature22383.

[63] Racle, J., de Jong, A., and Gfeller, D. (2019). Simultaneous prediction of MHC class I and II immunopeptidomes using deep learning. * bioRxiv preprint*. doi:10.1101/2020.06.08.140558.

[61] Lefranc, M.P. (2014). Immunoglobulin and T cell receptor genes: IMGT and the birth and rise of immunoinformatics. *Frontiers in Immunology*, 5, 22. doi:10.3389/fimmu.2014.00022.
