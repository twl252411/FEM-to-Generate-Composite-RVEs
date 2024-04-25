@echo off
call aba2020 cae noGUI=Explicit_Compression_Abaqus_2D_Single_S1
call aba2020 job=Job-1 cpus=64 int
call aba2020 cae noGUI=PostProcessing_ExtractCentroidsOriAngles_2D_S1
call aba2020 cae noGUI=FileCombination
call aba2020 cae noGUI=Explicit_Compression_Abaqus_2D_Single_S2
call aba2020 job=Job-2 cpus=64 int
call aba2020 cae noGUI=PostProcessing_ExtractCentroidsOriAngles_2D_S2