formatter = " %r %r %r %s"

print formatter % (1, 2, 3, 4)
print formatter % ('One', 'Two', 'Three', 'Four')
print formatter % ( True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it did not sing.",
	"So I said goodnight."
	)
