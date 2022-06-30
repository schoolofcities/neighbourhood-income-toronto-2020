<script>	
	
	import formerMun from "../data/formerMun.geo.json";
	import subwayLines from "../data/subwayLines.geo.json";
	import subwayStations from "../data/subwayStations.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";
	import tracts2020 from "../data/2020.geo.json";

	const coloursD = ["#DC4633", "#ee9d78", "#f2dfce", "#7eb4b3", "#007fa3"]
	
	export var currentLayer;

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = innerWidth * 40/80

	// let c1 = [-79.29, 43.70]
	// let c2 = [-78.89, 43.64]

	$: projection = geoMercator()
		.center([-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ])
		.scale([75000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);
	
	const params =	{
		"hhld_inc": {
			"name": "Household Income",
			"var_name": "ii16",
			"colours": coloursD,
			"ref_point": 102721 
		},	
		"ind_inc": {
			"name": "Individual Income",
			"var_name": "ih16",
			"colours": coloursD,
			"ref_point": 52268
		},
		"pov_lim": {
			"name": "Poverty Rate LIM",
			"var_name": "l16",
			"colours": coloursD,
			"ref_point": 16.3
			// 26.3
		}
	}

	$: colorDiv = scaleThreshold()
		.domain([
			params[currentLayer]["ref_point"] * 0.7,
			params[currentLayer]["ref_point"] * 0.85,
			params[currentLayer]["ref_point"] * 1.15,
			params[currentLayer]["ref_point"] * 1.3,
		])
		.range(coloursD);

	$: attributeName = params[currentLayer]["var_name"]

	$: features = tracts2020.features;
		
	$: features.map(item => {
	item.properties[attributeName]	
		? (item.properties.color = colorDiv(item.properties[attributeName]))
		: (item.properties.color = "white");
	});
	
	$: placeLabel = true;
	function labelToggle() {
		placeLabel = !placeLabel;
	}
	$: if (divWidth < 800) {
		placeLabel = false
	}
</script>



<div id="container" class="svg-container" bind:offsetWidth={divWidth}>

	<div id="labels">
		<button 
		id="label-button"
		class:label-selected="{placeLabel}"
		class:label-off="{divWidth < 800}"	
		on:click={labelToggle}>
			Labels
		</button>		
	</div>

	<svg width={innerWidth} height={height}	>
		{#each formerMun.features as data}
			<path id="fm-back" d={path(data)} />
		{/each}
		{#key attributeName}
		{#each features	as data}
			<path id="ct" d={path(data)} fill={data.properties.color} />
		{/each}
		{/key}
		{#each formerMun.features as data}
			<path id="fm" d={path(data)} />
		{/each}
		
		{#each subwayLines.features as data}
			<path id="subway-lines" d={path(data)} />
		{/each}
		{#each subwayStations.features as data}
			<circle
			class="subway-stop"
			cx={projection(data.geometry.coordinates)[0]}
			cy={projection(data.geometry.coordinates)[1]}
			r="2px"
			fill="black" />
		{/each}

		{#if placeLabel}	
			<text id="place-label" x="301" y="88">North York</text>
			<text id="place-label" x="389" y="243">East York</text>
			<text id="place-label" x="227" y="207">York</text>
			<text id="place-label" x="89" y="228">Etobicoke</text>
			<text id="place-label" x="519" y="163">Scarborough</text>
			<text id="place-label" x="297" y="287">Toronto</text>
		{/if}
	</svg>
	
</div>
	
<style>
	#container {
		width: 100%;
		max-width: 800px;
		min-width: 400px;
	}
	/* #meow {
		border: solid 1px rgb(243, 232, 232);
		border-bottom-right-radius: 100px;
	} */
	#fm-back {
		stroke: rgb(0, 0, 0);
		stroke-width: 5px;
		opacity: 0.08;
		fill-opacity: 0;
	}
	#ct {
		stroke: rgb(237, 237, 237);
		stroke-width: 1px;
	}
	#fm {
		stroke: rgb(36, 36, 36);
		stroke-width:1 px;
		fill-opacity: 0;
	}
	#subway-lines {
		fill-opacity: 0;
		stroke: rgb(0, 0, 0);
		stroke-width: 2px;
	}

	#place-label {
		font-size: 15px;
		fill: rgb(0, 0, 0);
		font-weight: bold;
		paint-order: stroke;
		stroke: #fff;
		stroke-opacity: 0.85;
		stroke-width: 4px;
		stroke-linecap: butt;
		stroke-linejoin: miter;
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
	#label-button {
		float: right;
		position: absolute;
		top: 25px;
		right: 20px;
		/* margin-right: 87px; */
		/* background-color: white; */
		border: solid 1px rgb(176, 176, 176);
		font-family: 	-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		color:  rgb(103, 103, 103);
		cursor: pointer;
		border-radius: 1px;
		padding: 4px;
		/* margin-bottom: -10px; */
	}
	#label-button:hover {
		color: #007fa3;
	}
	.label-selected {
		background-color: rgb(255, 255, 255);
	}
	.label-off {
		display: none;
	}
</style>
