# Galino_Gonzales_P-system-simulator

To simulate a P system with complex objects, we need to pay attention to two
components: generic rules and complex objects. As such, the input format for the
simulator will be as follows.
```json
{
	membranes: [Membrane]
}
```
The input will be a JSON object containing a single field: `membranes`.
`membranes` is a list of objects of type `Membrane`. The `Membrane` type
represent the membranes of the P system being simulated. Since the P system is
a single membrane system with no other membranes nested within it, we won't need
to think currently about how to represent nested membranes (although this could
be as easy as adding a `children` field to the `Membrane` type). 

## The `Membrane` type
The `Membrane` type has the following fields:
```json
{
	id: int
	generic_rules: [GenericRule]
	instantiated_rules: [InstantiatedRule],
	objects: [Object]
}
```
The `id` field represents the id of the membrane. The `generic_rules` field is
a list of objects of type `GenericRule`. This field represents the generic rules
that are contained in the current membraine. The `instantiated_rules` field is
a list of objects of type `InstantiatedRule`. This field serves as a container
for the rules that will be generated using the `GenericRule` objects in the
`generic_rules` field. The `objects` field is a list of `Object`, where each
`Object` will represent a generic object in the membrane. `Object` is actually
just an alias to `string`. We want to use strings to implement generic objects
because string methods and regex can make the implementation of pattern matching
much easier.

## The `GenericRule` type
The `GenericRule` type will have the following fields:
```json
{
	instantiation_mode: MIN | MAX,
	input: Object,
	output: Object,

	match(objects: [Object]) -> [InstantiatedRule]
}
```
The `instantiation_mode` field will represent the mode in which
`InstantiatedRule` objects will be generated from the generic rule. The value
of the field will either be `MIN` or `MAX`. The `input` field will represent
the left-hand side of a generic rule while the `output` field will represent
the right-hand side of the rule. Apart from the fields, the `GenericRule` type
will also have a method to it named `match`. The `match` method will accept a
list of `Object` and return a list of `InstantiatedRule` objects. The current
plan on the usage of this `match` method is that it will take in the entire
`objects` field of the `Membrane` type as its argument and return a list of
`InstantiatedRule` objects that will be appended the `instantiated_rules` list.
More info about this will be written on the section about simulator operation

## The `InstantiatedRule` type
The `InstantiatedRUle` type will have the following fields:
```json
{
	rewriting_mode: MIN | MAX,
	input: Object,
	output: Object,
}
```
The `rewriting_mode` field will represent the mode in which the
`InstantiatedRule`  will be applied to the objects in the `objects` field of
the `Membrane` type. The `input` field will represent the left-hand side of the
rule, while the `output` field will represent the right-hand side of the rule.
Application of the `InstantiatedRule` objects to the objects in the `objects`
field has still not been finalized yet, although I suggest that we could also
add a method to apply the rule on the objects that will take in a list of `Object` as argument
and return a list of `Object`, similar to the `match` method in `GenericRule`.

## How will the simulator work?
The following steps are how the simulator is currently envisioned to work.
1. The simulator will take in and parse the input as described above.
2. A loop will be created to process each membrane. 
3. In each iteration of the loop, a `GenericRule` object will be processed. 
   The `GenericRule` object will call its `match` method, taking in the `objects`
   field as its argument to generate instantiated rules in the `instantiated_rules`
   list.
4. Apply all instantiated rules on the objects in the `objects` field.
5. Proceed to next membrane.

The stopping condition of the loop should be when there are no more changes from
the `p(b)` object to the `p(w)` object. As such, when the rule involving the
`p(b)` to `p(w)` transition is being applied, the number of changes should be
kept track.
 
