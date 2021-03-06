# -*- coding: utf-8 -*-

__author__ = 'Asger Bachmann (agb@birc.au.dk)'


class Dataset:
    def __init__(self, option, name, name_column, columns):
        self.option = option
        self.name = name
        self.name_column = name_column
        self.columns = columns


ljgea_gene = Dataset("ljgea-geneid", "expat_ljgea_geneid", "GeneID", [
    #"GeneID",
    "Mean_WT_control1", "Mean_WT_Drought1", "Mean_Ljgln2_2_Control1", "Mean_Ljgln2_2_Drought1",
    "Mean_root_4dpicontrol1B", "Mean_root_4dpimycorrhized1D", "Mean_root_28dpicontrol1A",
    "Mean_root_28dpimycorrhized1C", "Mean_WT_root_tip_3w_uninocul_1", "Mean_WT_root_3w_uninocul_1",
    "Mean_WT_root_3w_5mM_nitrate_1", "Mean_WT_root_6w_5mM_nitrate_1", "Mean_WT_shoot_3w_5mM_nitrate_1",
    "Mean_WT_shoot_3w_uninocul_1", "Mean_WT_shoot_3w_inocul3_1", "Mean_WT_leaf_6w_5mM_nitrate_1",
    "Mean_WT_stem_6w_5mM_nitrate_1", "Mean_WT_flower_13w_5mM_nitrate_1", "Mean_har1_root_3w_uninocul_2",
    "Mean_har1_root_3w_inocul3_2", "Mean_har1_shoot_3w_uninocul_1", "Mean_har1_shoot_3w_inocul3_1",
    "Mean_WT_root_3w_nodC_inocul1_1", "Mean_WT_root_3w_inocul1_1", "Mean_WT_root_3w_inocul3_1",
    "Mean_WT_nodule_3w_inocul14_1", "Mean_WT_nodule_3w_inocul21_1", "Mean_WT_root_nodule_3w_inocul7_1",
    "Mean_WT_root_nodule_3w_inocul21_1", "Mean_WT_rootSZ_3w_uninocul_1",
    "Mean_WT_rootSZ_3w_Nod_inocul1_1", "Mean_WT_rootSZ_3w_inocul1_1", "Mean_nfr5_rootSZ_3w_uninocul_1",
    "Mean_nfr5_rootSZ_3w_inocul1_1", "Mean_nfr1_rootSZ_3w_uninocul_1", "Mean_nfr1_rootSZ_3w_inocul1_1",
    "Mean_nup133_rootSZ_3w_uninocul_1", "Mean_nup133_rootSZ_3w_inocul1_1",
    "Mean_cyclops_root_3w_uninocul", "Mean_cyclops_root_nodule_3w_inocul21",
    "Mean_nin_rootSZ_3w_uninocul_1", "Mean_nin_rootSZ_3w_inocul1_1", "Mean_sen1_root_3w_uninocul_1",
    "Mean_sen1_nodule_3w_inocul21_1", "Mean_sst1_root_3w_uninocul_1", "Mean_sst1_nodule_3w_inocul21_1",
    "Mean_cyclops_root_3w_inocul", "Mean_Shoot_0mM_sodiumChloride_1",
    "Mean_Shoot_25mM_sodiumChloride_Initial_1", "Mean_Shoot_50mM_sodiumChloride_Initial_1",
    "Mean_Shoot_75mM_sodiumChloride_Initial_1", "Mean_Shoot_50mM_sodiumChloride_Gradual_1",
    "Mean_Shoot_100mM_sodiumChloride_Gradual_1", "Mean_Shoot_150mM_sodiumChloride_Gradual_1",
    "Mean_Lburttii_Ctrol_A", "Mean_Lburttii_Salt_A", "Mean_Lcorniculatus_Ctrol_A",
    "Mean_Lcorniculatus_Salt_A", "Mean_Lfilicaulis_Ctrol_A", "Mean_Lfilicaulis_Salt_A",
    "Mean_Lglaber_Ctrol_A", "Mean_Lglaber_Salt_A", "Mean_Ljaponicus_Gifu_Ctrol_A",
    "Mean_Ljaponicus_Gifu_Salt_A", "Mean_Ljaponicus_MG20_Ctrol_A", "Mean_Ljaponicus_MG20_Salt_A",
    "Mean_Luliginosus_Ctrol_A", "Mean_Luliginosus_Salt_A", "Mean_Fl_1", "Mean_Pod20_1", "Mean_Seed10d_1",
    "Mean_Seed12d_1", "Mean_Seed14d_1", "Mean_Seed16d_1", "Mean_Seed20d_1", "Mean_Leaf_1", "Mean_Pt_1",
    "Mean_Stem_1", "Mean_Root_1", "Mean_Root0h_1", "Mean_Nod21_1"
])

ljgea_probe = Dataset("ljgea-probeid", "expat_ljgea_probeid", "ProbeID", [
    #"ProbeID",
    "Mean_Seed10d_1", "Mean_Seed12d_1", "Mean_Seed14d_1", "Mean_Seed16d_1", "Mean_Seed20d_1", "Mean_Pod20_1",
    "Mean_Fl_1", "Mean_WT_control1", "Mean_WT_Drought1", "Mean_Ljgln2_2_Control1", "Mean_Ljgln2_2_Drought1",
    "Mean_WT_shoot_3w_5mM_nitrate_1", "Mean_WT_shoot_3w_uninocul_1", "Mean_WT_shoot_3w_inocul3_1",
    "Mean_har1_shoot_3w_inocul3_1", "Mean_Shoot_0mM_sodiumChloride_1", "Mean_Shoot_25mM_sodiumChloride_Initial_1",
    "Mean_Shoot_50mM_sodiumChloride_Initial_1", "Mean_Shoot_75mM_sodiumChloride_Initial_1",
    "Mean_Shoot_50mM_sodiumChloride_Gradual_1", "Mean_Shoot_100mM_sodiumChloride_Gradual_1",
    "Mean_Shoot_150mM_sodiumChloride_Gradual_1", "Mean_Lburttii_Ctrol_A", "Mean_Lburttii_Salt_A",
    "Mean_Lcorniculatus_Ctrol_A", "Mean_Lcorniculatus_Salt_A", "Mean_Lfilicaulis_Ctrol_A", "Mean_Lfilicaulis_Salt_A",
    "Mean_Lglaber_Ctrol_A", "Mean_Lglaber_Salt_A", "Mean_Ljaponicus_Gifu_Ctrol_A", "Mean_Ljaponicus_Gifu_Salt_A",
    "Mean_Ljaponicus_MG20_Ctrol_A", "Mean_Ljaponicus_MG20_Salt_A", "Mean_Luliginosus_Ctrol_A",
    "Mean_Luliginosus_Salt_A", "Mean_Pt_1", "Mean_WT_leaf_6w_5mM_nitrate_1", "Mean_Leaf_1",
    "Mean_WT_stem_6w_5mM_nitrate_1", "Mean_Stem_1", "Mean_root_4dpicontrol1B", "Mean_root_28dpicontrol1A",
    "Mean_WT_root_tip_3w_uninocul_1", "Mean_WT_root_3w_uninocul_1", "Mean_har1_root_3w_uninocul_2",
    "Mean_nin_rootSZ_3w_uninocul_1", "Mean_sen1_root_3w_uninocul_1", "Mean_sst1_root_3w_uninocul_1", "Mean_Root_1",
    "Mean_Root0h_1", "Mean_nfr5_rootSZ_3w_uninocul_1", "Mean_nfr1_rootSZ_3w_uninocul_1",
    "Mean_nup133_rootSZ_3w_uninocul_1", "Mean_WT_root_3w_5mM_nitrate_1", "Mean_WT_root_6w_5mM_nitrate_1",
    "Mean_root_4dpimycorrhized1D", "Mean_root_28dpimycorrhized1C", "Mean_har1_root_3w_inocul3_2",
    "Mean_WT_root_3w_nodC_inocul1_1", "Mean_WT_root_3w_inocul1_1", "Mean_WT_root_3w_inocul3_1",
    "Mean_WT_rootSZ_3w_Nod_inocul1_1", "Mean_WT_rootSZ_3w_inocul1_1", "Mean_nfr5_rootSZ_3w_inocul1_1",
    "Mean_nfr1_rootSZ_3w_inocul1_1", "Mean_nup133_rootSZ_3w_inocul1_1", "Mean_nin_rootSZ_3w_inocul1_1",
    "Mean_WT_nodule_3w_inocul14_1", "Mean_WT_nodule_3w_inocul21_1", "Mean_sen1_nodule_3w_inocul21_1",
    "Mean_sst1_nodule_3w_inocul21_1", "Mean_Nod21_1", "Mean_WT_root_nodule_3w_inocul21_1"
])

simon_kelly_bacteria = Dataset("rnaseq-kellys-2015-bacteria", "expat_RNAseq_KellyS_bacteria", "TranscriptID", [
    #"TranscriptID",
    "Mean_277_exoU_24", "Mean_277_exoU_72", "Mean_277_exoYF_24", "Mean_277_exoYF_72", "Mean_277_H2O_24",
    "Mean_277_nodC_24", "Mean_277_R7A_24", "Mean_277_R7A_72", "Mean_311_exoU_24", "Mean_311_exoU_72",
    "Mean_311_exoYF_24", "Mean_311_exoYF_72", "Mean_311_H2O_24", "Mean_311_nodC_24", "Mean_311_R7A_24",
    "Mean_311_R7A_72", "Mean_G_exoU_24", "Mean_G_exoU_72", "Mean_G_exoYF_24", "Mean_G_exoYF_72", "Mean_G_H2O_24",
    "Mean_G_nodC_24", "Mean_G_R7A_24", "Mean_G_R7A_72"
])

simon_kelly_purified_compounds = Dataset("rnaseq-kellys-2015-purifiedcompounds", "expat_RNAseq_KellyS_purifiedcompounds", "TranscriptID", [
    #"TranscriptID",
    "Mean_G_H2O_24", "Mean_277_H2O_24", "Mean_311_H2O_24", "Mean_G_NF_24", "Mean_277_NF_24", "Mean_311_NF_24",
    "Mean_G_R7AEPS_24", "Mean_277_R7AEPS_24", "Mean_311_R7AEPS_24", "Mean_G_UEPS_24", "Mean_277_UEPS_24",
    "Mean_311_UEPS_24", "Mean_G_NF_R7AEPS_24", "Mean_277_NF_R7AEPS_24", "Mean_311_NF_R7AEPS_24", "Mean_G_NF_UEPS_24",
    "Mean_277_NF_UEPS_24", "Mean_311_NF_UEPS_24"
])

simon_kelly_2017 = Dataset("rnaseq-kellys-2017-microbialspectrum", "expat_RNAseq_KellyS2017_MicrobialSpectrum", "GeneID", [
    #"GeneID",
    "Mean_RootHair_H2O_1dpi",
    "Mean_RootHair_nodC_1dpi",
    "Mean_RootHair_R7A_1dpi",
    "Mean_RootHair_R7A_3dpi",
    "Mean_RootHair_NF_1dpi",
    "Mean_NodulePrimordia_R7A_7dpi",
    "Mean_Nodule_R7A_21dpi",
    "Mean_Root_H2O_1dpi",
    "Mean_Root_H2O_3dpi",
    "Mean_Root_Ml_R7A_1dpi",
    "Mean_Root_Ml_R7A_3dpi",
    "Mean_Root_Sf_HH103_1dpi",
    "Mean_Root_Sf_HH103_3dpi",
    "Mean_Root_Be_1dpi",
    "Mean_Root_Be_3dpi",
    "Mean_Root_Pst_DC3000_1dpi",
    "Mean_Root_Pst_DC3000_3dpi",
    "Mean_Root_Rs_JS763_1dpi",
    "Mean_Root_Rs_JS763_3dpi"
])

all_by_name = {
    u"ljgea-geneid": ljgea_gene,
    u"ljgea-probeid": ljgea_probe,
    u"rnaseq-kellys-2015-bacteria": simon_kelly_bacteria,
    u"rnaseq-kellys-2015-purifiedcompounds": simon_kelly_purified_compounds,
    u"rnaseq-kellys-2017-microbialspectrum": simon_kelly_2017
}
