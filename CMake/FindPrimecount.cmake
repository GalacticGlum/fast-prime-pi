set(Primecount_INCLUDE_DIRS "${PPiCCG_DEPEND_DIR}/primecount/include")
set(Primecount_LIBRARIES 
	"${PPiCCG_DEPEND_DIR}/primecount/lib/${_config}/Win32/primecount.lib"
	"${PPiCCG_DEPEND_DIR}/primecount/lib/${_config}/Win32/primesieve.lib"
)

# Check if we found it!
IF ( Primecount_INCLUDE_DIRS AND Primecount_LIBRARIES )
	SET( Primecount_FOUND TRUE )
	MESSAGE( STATUS "Looking for Primecount - found" )
ELSE ( Primecount_INCLUDE_DIRS AND Primecount_LIBRARIES )
	SET( Primecount_FOUND FALSE )
	MESSAGE( STATUS "Looking for Primecount - not found" )
ENDIF ( Primecount_INCLUDE_DIRS AND Primecount_LIBRARIES )