<script>
	export var coloursDiv;
</script>

<div class="dif-legend">
	<svg width="300" height="75">
		<text class="legend-title" x="11" y="15">Percent change from 2015 to 2020</text>
		<text class="legend-label" x="30" y="35">-30%</text>
		<text class="legend-label" x="75" y="35">-15%</text>
		<text class="legend-label" x="120" y="35">+15%</text>
		<text class="legend-label" x="165" y="35">+30%</text>
		<rect class="box" width="45" height = "15" x="0" y="40" style="fill:{coloursDiv[0]}; stroke: rgb(206, 206, 206);"></rect>
		<rect class="box" width="45" height = "15" x="45" y="40" style="fill:{coloursDiv[1]}; stroke: rgb(206, 206, 206);"></rect>
		<rect class="box" width="45" height = "15" x="90" y="40" style="fill:{coloursDiv[2]}; stroke: rgb(206, 206, 206);"></rect>
		<rect class="box" width="45" height = "15" x="135" y="40" style="fill:{coloursDiv[3]}; stroke: rgb(206, 206, 206);"></rect>
		<rect class="box" width="45" height = "15" x="180" y="40" style="fill:{coloursDiv[4]}; stroke: rgb(206, 206, 206);"></rect>
	</svg>
</div>

<style>
	.dif-legend {
		margin: auto;
		height: 75px;
		max-width: 600px;
		width: 100%;
	}
	.legend-label {
		font-size: 13px;
		fill: rgb(66, 66, 66);
	}
	.legend-title {
		font-size: 13px;
		fill: rgb(17, 17, 17);
	}
	@media (max-width:620px) {
		.dif-legend {
			padding-left: 25px;
			width: calc(100% - 25px);
		}
	}
</style>
