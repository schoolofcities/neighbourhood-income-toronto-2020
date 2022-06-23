<script>

import { json } from "d3";
import Marks from "./Marks.svelte";
import inc1961 from "../data/1961.json";

let dataset = inc1961.features;
console.log(dataset)

// let dataset = [];
//   json(
//     "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
//   ).then((data) => {
//     dataset = data.features;
//   });

const width = 1200, height = 600;
</script>

<main>
  <svg {width} {height} id="meow">
    <Marks {dataset} />
  </svg>
</main>

<style>
	/* main {
		background-color: aquamarine;
	}
	#meow {
		background-color: antiquewhite;
	} */
</style>
