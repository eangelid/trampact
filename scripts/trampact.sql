SELECT * FROM BD_GENT_2006

SELECT * FROM BD_GENT_2016

SELECT * FROM iris_T1 order by iris_id 

SELECT iris_id, NOM_IRIS FROM iris_T2 order by iris_id 

SELECT BD_GENT_2006.* 
FROM BD_GENT_2006, iris_T1 
WHERE BD_GENT_2006.iris_id = iris_T1.iris_id 
ORDER BY iris_id 

SELECT BD_GENT_2016.* 
FROM BD_GENT_2016, iris_T1 
WHERE BD_GENT_2016.iris_id = iris_T1.iris_id 
ORDER BY iris_id 

SELECT 
	iris_id
	,tx_chom_2006
	,tx_empl_2006
	,tx_ouvr_2006
	,tx_TP_2006
	,tx_HLM_2006
	,tx_no_transp_2006
	,tx_walk_2006
	,tx_moto_2006
	,tx_voit_2006
	,tx_TC_2006
	,tx_HH_moins2ans_2006
	,tx_HH_2_4ans_2006
	,tx_HH_5_9ans_2006
	,tx_HH_plus10ans_2006
	,tx_HH_with_park_2006
	,tx_HH_with_voit_2006
	,tx_HH_1voit_2006
	,tx_HH_2voit_2006
	,tx_empl_prec_2006
FROM BD_GENT_2006
WHERE
	tx_chom_2006 > 100
	OR tx_empl_2006 > 100
	OR tx_ouvr_2006 > 100
	OR tx_TP_2006 > 100
	OR tx_HLM_2006 > 100
	OR tx_no_transp_2006 > 100
	OR tx_walk_2006 > 100
	OR tx_moto_2006 > 100
	OR tx_voit_2006 > 100
	OR tx_TC_2006 > 100
	OR tx_HH_moins2ans_2006 > 100
	OR tx_HH_2_4ans_2006 > 100
	OR tx_HH_5_9ans_2006 > 100
	OR tx_HH_plus10ans_2006 > 100
/*
	OR tx_HH_with_park_2006 > 100
	OR tx_HH_with_voit_2006 > 100
	OR tx_HH_1voit_2006 > 100
	OR tx_HH_2voit_2006 > 100
	OR tx_empl_prec_2006 > 100
*/
ORDER BY
	iris_id 
