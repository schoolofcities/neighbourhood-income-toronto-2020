<script>	
	
	import formerMun from "../data/formerMun.geo.json";
	import subwayLines from "../data/subwayLines.geo.json";
	import subwayStations from "../data/subwayStations.geo.json";
	import { geoPath, geoMercator, scaleThreshold } from "d3";
	import tracts2020 from "../data/2020.geo.json";

	export var coloursD;	
	export var currentLayer;

	let divWidth = 800;
	$: innerWidth = divWidth;
	$: height = innerWidth * 40/80

	// let c1 = [-79.29, 43.70]
	// let c2 = [-78.89, 43.64]
	// [-0.001* innerWidth - 78.49, 0.00015 * innerWidth + 43.58 ]
	// let c600 = [-79.145,43.68]

	$: projection = geoMercator()
		.center([-78.17 - 0.0023*innerWidth + 0.000001125*innerWidth**2, 43.5 + 0.00045*innerWidth - 2.5e-7*innerWidth**2])
		.scale([75000 * innerWidth / 800])
		.angle([-17]);
	$: path = geoPath(projection);
	
	$: colorDiv = scaleThreshold()
		.domain([-30,-15,15,30])
		.range(coloursD);
	
	// $: attributeName = params[currentLayer]["var_name"]

	$: features = tracts2020.features;
		
	$: features.map(item => {
	item.properties["ih21"]	> 0
		? (item.properties.colourC = colorDiv(
			100 * (+(item.properties["ih21"]) - +(item.properties["ih16"])) / (+(item.properties["ih16"]))
			))
		: (item.properties.colourC = "white");
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
		{#key currentLayer}
		{#each features	as data}
			<path id="ct" d={path(data)} fill={data.properties.colourC} />
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
		/* min-width: 400px; */
	}
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
		border: solid 1px rgb(176, 176, 176);
		font-family: 	-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,	 Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
		color:  rgb(103, 103, 103);
		cursor: pointer;
		border-radius: 1px;
		padding: 4px;
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
