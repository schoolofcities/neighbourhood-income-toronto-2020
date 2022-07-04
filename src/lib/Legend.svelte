<script>
	export var colours;
	export var title1;
	export var title2;
	export var labels;
</script>

<svg width="400" height="200">
	<text class="legend-title" x="8" y="22">{title1} </text>
	<text class="legend-title" x="8" y="38">{title2}</text>

	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="50"
		style="fill:{colours[0]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="70"
		style="fill:{colours[1]};"
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
		style="fill:{colours[3]};"
	/>
	<rect
		class="box"
		width="30"
		height="15"
		x="10"
		y="130"
		style="fill:{colours[4]}"
	/>

	<text class="legend-label" x="45" y="62">{labels[0]}</text>
	<text class="legend-label" x="45" y="82">{labels[1]}</text>
	<text class="legend-label" x="45" y="102">{labels[2]}</text>
	<text class="legend-label" x="45" y="122">{labels[3]}</text>
	<text class="legend-label" x="45" y="142">{labels[4]}</text>
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
