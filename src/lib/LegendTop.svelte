<script>
	export var layer;
	export var coloursDiv;
	export var coloursSeqBlue;
	export var coloursSeqRed;

	$: colours = coloursDiv
	$: title1 = "Census tract average household"
	$: title2 = "income in 2020"
	$: labels = [
		"Less than $75,000",
		"$75,000 to $90,000",
		"$90,000 to $100,000",
		"$100,000 to $115,000",
		"More than $115,000"
	]

	$: if (layer === "ind_inc") {
		colours = coloursDiv
		title1 = "Census tract average individual income in 2020" 
		title2 = "among income recipients aged 15 years and up"
		labels = [
			"Less than $35,000",
			"$35,000 to $50,000",
			"$50,000 to $65,000",
			"$65,000 to $80,000",
			"More than $80,000"
		]
	} 
	else if (layer === "hhld_inc") {
		colours = coloursDiv
		title1 = "Census tract average household"
		title2 = "income in 2020"
		labels = [
			"Less than $75,000",
			"$75,000 to $90,000",
			"$90,000 to $100,000",
			"$100,000 to $115,000",
			"More than $115,000"
		]
	}
	else if (layer === "hhld_inc_m") {
		colours = coloursDiv
		title1 = "Census tract median household"
		title2 = "income in 2020"
		labels = [
			"Less than $55,000",
			"$55,000 to $70,000",
			"$70,000 to $85,000",
			"$85,000 to $100,000",
			"More than $100,000"
		]
	}
	else if (layer === "ind_inc_m") {
		colours = coloursDiv
		title1 = "Census tract median individual income in 2020" 
		title2 = "among income recipients aged 15 years and up"
		labels = [
			"Less than $30,000",
			"$30,000 to $40,000",
			"$40,000 to $50,000",
			"$50,000 to $60,000",
			"More than $60,000"
		]
	}
	else if (layer === "pop_den") {
		colours = coloursSeqBlue
		title1 = "Population density by census tract"
		title2 = "(persons per square km)"
		labels = [
			"0 to 1,000",
			"1,000 to 4,000",
			"4,000 to 7,000",
			"7,000 to 10,000",
			"More than 10,000"
		]
	}
	else {
		colours = coloursSeqRed
		title1 = "Poverty rate by census tract based on the"
		title2 = "after-tax Low-Income Measure (LIM)"
		labels = [
			"Less than 10%",
			"10% to 15%",
			"15% to 20%",
			"20% to 25%",
			"More than 25%"
		]
	}
	
	
</script>

<svg width="300" height="150">
	<text class="legend-title" x="8" y="22">{title1} </text>
	<text class="legend-title" x="8" y="38">{title2}</text>

	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="50"
		style="fill:{colours[4]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="70"
		style="fill:{colours[3]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="90"
		style="fill:{colours[2]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="110"
		style="fill:{colours[1]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="130"
		style="fill:{colours[0]}"
	/>

	<text class="legend-label" x="45" y="62">{labels[4]}</text>
	<text class="legend-label" x="45" y="82">{labels[3]}</text>
	<text class="legend-label" x="45" y="102">{labels[2]}</text>
	<text class="legend-label" x="45" y="122">{labels[1]}</text>
	<text class="legend-label" x="45" y="142">{labels[0]}</text>
</svg>

<style>
	.box {
		stroke-width: 1px;
		stroke: rgb(206, 206, 206);
	}
	.legend-label {
		font-size: 13px;
		fill: rgb(66, 66, 66);
	}
	.legend-title {
		font-size: 13px;
		fill: rgb(17, 17, 17);
	}
</style>
