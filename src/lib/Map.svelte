<script>

import { json } from "d3";
import Marks from "./Marks.svelte";
import inc1961 from "../data/1961.geo.json";
import formerMun from "../data/formerMun5.geo.json"

let dataset = inc1961.features;
console.log(dataset);

console.log(formerMun.features);

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
