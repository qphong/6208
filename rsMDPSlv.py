# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rsMDPSlv', [dirname(__file__)])
        except ImportError:
            import _rsMDPSlv
            return _rsMDPSlv
        if fp is not None:
            try:
                _mod = imp.load_module('_rsMDPSlv', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rsMDPSlv = swig_import_helper()
    del swig_import_helper
else:
    import _rsMDPSlv
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _rsMDPSlv.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _rsMDPSlv.SwigPyIterator_value(self)
    def incr(self, n=1): return _rsMDPSlv.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _rsMDPSlv.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _rsMDPSlv.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _rsMDPSlv.SwigPyIterator_equal(self, *args)
    def copy(self): return _rsMDPSlv.SwigPyIterator_copy(self)
    def next(self): return _rsMDPSlv.SwigPyIterator_next(self)
    def __next__(self): return _rsMDPSlv.SwigPyIterator___next__(self)
    def previous(self): return _rsMDPSlv.SwigPyIterator_previous(self)
    def advance(self, *args): return _rsMDPSlv.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _rsMDPSlv.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _rsMDPSlv.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _rsMDPSlv.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _rsMDPSlv.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _rsMDPSlv.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _rsMDPSlv.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _rsMDPSlv.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vec_str(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec_str, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec_str, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.vec_str_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.vec_str___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.vec_str___bool__(self)
    def __len__(self): return _rsMDPSlv.vec_str___len__(self)
    def pop(self): return _rsMDPSlv.vec_str_pop(self)
    def __getslice__(self, *args): return _rsMDPSlv.vec_str___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlv.vec_str___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlv.vec_str___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.vec_str___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlv.vec_str___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlv.vec_str___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlv.vec_str_append(self, *args)
    def empty(self): return _rsMDPSlv.vec_str_empty(self)
    def size(self): return _rsMDPSlv.vec_str_size(self)
    def clear(self): return _rsMDPSlv.vec_str_clear(self)
    def swap(self, *args): return _rsMDPSlv.vec_str_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.vec_str_get_allocator(self)
    def begin(self): return _rsMDPSlv.vec_str_begin(self)
    def end(self): return _rsMDPSlv.vec_str_end(self)
    def rbegin(self): return _rsMDPSlv.vec_str_rbegin(self)
    def rend(self): return _rsMDPSlv.vec_str_rend(self)
    def pop_back(self): return _rsMDPSlv.vec_str_pop_back(self)
    def erase(self, *args): return _rsMDPSlv.vec_str_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_vec_str(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlv.vec_str_push_back(self, *args)
    def front(self): return _rsMDPSlv.vec_str_front(self)
    def back(self): return _rsMDPSlv.vec_str_back(self)
    def assign(self, *args): return _rsMDPSlv.vec_str_assign(self, *args)
    def resize(self, *args): return _rsMDPSlv.vec_str_resize(self, *args)
    def insert(self, *args): return _rsMDPSlv.vec_str_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlv.vec_str_reserve(self, *args)
    def capacity(self): return _rsMDPSlv.vec_str_capacity(self)
    __swig_destroy__ = _rsMDPSlv.delete_vec_str
    __del__ = lambda self : None;
vec_str_swigregister = _rsMDPSlv.vec_str_swigregister
vec_str_swigregister(vec_str)

class map_str_vecStr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_str_vecStr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_str_vecStr, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.map_str_vecStr_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.map_str_vecStr___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.map_str_vecStr___bool__(self)
    def __len__(self): return _rsMDPSlv.map_str_vecStr___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _rsMDPSlv.map_str_vecStr___getitem__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.map_str_vecStr___delitem__(self, *args)
    def has_key(self, *args): return _rsMDPSlv.map_str_vecStr_has_key(self, *args)
    def keys(self): return _rsMDPSlv.map_str_vecStr_keys(self)
    def values(self): return _rsMDPSlv.map_str_vecStr_values(self)
    def items(self): return _rsMDPSlv.map_str_vecStr_items(self)
    def __contains__(self, *args): return _rsMDPSlv.map_str_vecStr___contains__(self, *args)
    def key_iterator(self): return _rsMDPSlv.map_str_vecStr_key_iterator(self)
    def value_iterator(self): return _rsMDPSlv.map_str_vecStr_value_iterator(self)
    def __setitem__(self, *args): return _rsMDPSlv.map_str_vecStr___setitem__(self, *args)
    def asdict(self): return _rsMDPSlv.map_str_vecStr_asdict(self)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_map_str_vecStr(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _rsMDPSlv.map_str_vecStr_empty(self)
    def size(self): return _rsMDPSlv.map_str_vecStr_size(self)
    def clear(self): return _rsMDPSlv.map_str_vecStr_clear(self)
    def swap(self, *args): return _rsMDPSlv.map_str_vecStr_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.map_str_vecStr_get_allocator(self)
    def begin(self): return _rsMDPSlv.map_str_vecStr_begin(self)
    def end(self): return _rsMDPSlv.map_str_vecStr_end(self)
    def rbegin(self): return _rsMDPSlv.map_str_vecStr_rbegin(self)
    def rend(self): return _rsMDPSlv.map_str_vecStr_rend(self)
    def count(self, *args): return _rsMDPSlv.map_str_vecStr_count(self, *args)
    def erase(self, *args): return _rsMDPSlv.map_str_vecStr_erase(self, *args)
    def find(self, *args): return _rsMDPSlv.map_str_vecStr_find(self, *args)
    def lower_bound(self, *args): return _rsMDPSlv.map_str_vecStr_lower_bound(self, *args)
    def upper_bound(self, *args): return _rsMDPSlv.map_str_vecStr_upper_bound(self, *args)
    __swig_destroy__ = _rsMDPSlv.delete_map_str_vecStr
    __del__ = lambda self : None;
map_str_vecStr_swigregister = _rsMDPSlv.map_str_vecStr_swigregister
map_str_vecStr_swigregister(map_str_vecStr)

class map_2str_vecStr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_2str_vecStr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_2str_vecStr, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.map_2str_vecStr_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.map_2str_vecStr___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.map_2str_vecStr___bool__(self)
    def __len__(self): return _rsMDPSlv.map_2str_vecStr___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _rsMDPSlv.map_2str_vecStr___getitem__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.map_2str_vecStr___delitem__(self, *args)
    def has_key(self, *args): return _rsMDPSlv.map_2str_vecStr_has_key(self, *args)
    def keys(self): return _rsMDPSlv.map_2str_vecStr_keys(self)
    def values(self): return _rsMDPSlv.map_2str_vecStr_values(self)
    def items(self): return _rsMDPSlv.map_2str_vecStr_items(self)
    def __contains__(self, *args): return _rsMDPSlv.map_2str_vecStr___contains__(self, *args)
    def key_iterator(self): return _rsMDPSlv.map_2str_vecStr_key_iterator(self)
    def value_iterator(self): return _rsMDPSlv.map_2str_vecStr_value_iterator(self)
    def __setitem__(self, *args): return _rsMDPSlv.map_2str_vecStr___setitem__(self, *args)
    def asdict(self): return _rsMDPSlv.map_2str_vecStr_asdict(self)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_map_2str_vecStr(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _rsMDPSlv.map_2str_vecStr_empty(self)
    def size(self): return _rsMDPSlv.map_2str_vecStr_size(self)
    def clear(self): return _rsMDPSlv.map_2str_vecStr_clear(self)
    def swap(self, *args): return _rsMDPSlv.map_2str_vecStr_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.map_2str_vecStr_get_allocator(self)
    def begin(self): return _rsMDPSlv.map_2str_vecStr_begin(self)
    def end(self): return _rsMDPSlv.map_2str_vecStr_end(self)
    def rbegin(self): return _rsMDPSlv.map_2str_vecStr_rbegin(self)
    def rend(self): return _rsMDPSlv.map_2str_vecStr_rend(self)
    def count(self, *args): return _rsMDPSlv.map_2str_vecStr_count(self, *args)
    def erase(self, *args): return _rsMDPSlv.map_2str_vecStr_erase(self, *args)
    def find(self, *args): return _rsMDPSlv.map_2str_vecStr_find(self, *args)
    def lower_bound(self, *args): return _rsMDPSlv.map_2str_vecStr_lower_bound(self, *args)
    def upper_bound(self, *args): return _rsMDPSlv.map_2str_vecStr_upper_bound(self, *args)
    __swig_destroy__ = _rsMDPSlv.delete_map_2str_vecStr
    __del__ = lambda self : None;
map_2str_vecStr_swigregister = _rsMDPSlv.map_2str_vecStr_swigregister
map_2str_vecStr_swigregister(map_2str_vecStr)

class map_str_dbl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_str_dbl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_str_dbl, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.map_str_dbl_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.map_str_dbl___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.map_str_dbl___bool__(self)
    def __len__(self): return _rsMDPSlv.map_str_dbl___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _rsMDPSlv.map_str_dbl___getitem__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.map_str_dbl___delitem__(self, *args)
    def has_key(self, *args): return _rsMDPSlv.map_str_dbl_has_key(self, *args)
    def keys(self): return _rsMDPSlv.map_str_dbl_keys(self)
    def values(self): return _rsMDPSlv.map_str_dbl_values(self)
    def items(self): return _rsMDPSlv.map_str_dbl_items(self)
    def __contains__(self, *args): return _rsMDPSlv.map_str_dbl___contains__(self, *args)
    def key_iterator(self): return _rsMDPSlv.map_str_dbl_key_iterator(self)
    def value_iterator(self): return _rsMDPSlv.map_str_dbl_value_iterator(self)
    def __setitem__(self, *args): return _rsMDPSlv.map_str_dbl___setitem__(self, *args)
    def asdict(self): return _rsMDPSlv.map_str_dbl_asdict(self)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_map_str_dbl(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _rsMDPSlv.map_str_dbl_empty(self)
    def size(self): return _rsMDPSlv.map_str_dbl_size(self)
    def clear(self): return _rsMDPSlv.map_str_dbl_clear(self)
    def swap(self, *args): return _rsMDPSlv.map_str_dbl_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.map_str_dbl_get_allocator(self)
    def begin(self): return _rsMDPSlv.map_str_dbl_begin(self)
    def end(self): return _rsMDPSlv.map_str_dbl_end(self)
    def rbegin(self): return _rsMDPSlv.map_str_dbl_rbegin(self)
    def rend(self): return _rsMDPSlv.map_str_dbl_rend(self)
    def count(self, *args): return _rsMDPSlv.map_str_dbl_count(self, *args)
    def erase(self, *args): return _rsMDPSlv.map_str_dbl_erase(self, *args)
    def find(self, *args): return _rsMDPSlv.map_str_dbl_find(self, *args)
    def lower_bound(self, *args): return _rsMDPSlv.map_str_dbl_lower_bound(self, *args)
    def upper_bound(self, *args): return _rsMDPSlv.map_str_dbl_upper_bound(self, *args)
    __swig_destroy__ = _rsMDPSlv.delete_map_str_dbl
    __del__ = lambda self : None;
map_str_dbl_swigregister = _rsMDPSlv.map_str_dbl_swigregister
map_str_dbl_swigregister(map_str_dbl)

class map_2str_dbl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_2str_dbl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_2str_dbl, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.map_2str_dbl_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.map_2str_dbl___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.map_2str_dbl___bool__(self)
    def __len__(self): return _rsMDPSlv.map_2str_dbl___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _rsMDPSlv.map_2str_dbl___getitem__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.map_2str_dbl___delitem__(self, *args)
    def has_key(self, *args): return _rsMDPSlv.map_2str_dbl_has_key(self, *args)
    def keys(self): return _rsMDPSlv.map_2str_dbl_keys(self)
    def values(self): return _rsMDPSlv.map_2str_dbl_values(self)
    def items(self): return _rsMDPSlv.map_2str_dbl_items(self)
    def __contains__(self, *args): return _rsMDPSlv.map_2str_dbl___contains__(self, *args)
    def key_iterator(self): return _rsMDPSlv.map_2str_dbl_key_iterator(self)
    def value_iterator(self): return _rsMDPSlv.map_2str_dbl_value_iterator(self)
    def __setitem__(self, *args): return _rsMDPSlv.map_2str_dbl___setitem__(self, *args)
    def asdict(self): return _rsMDPSlv.map_2str_dbl_asdict(self)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_map_2str_dbl(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _rsMDPSlv.map_2str_dbl_empty(self)
    def size(self): return _rsMDPSlv.map_2str_dbl_size(self)
    def clear(self): return _rsMDPSlv.map_2str_dbl_clear(self)
    def swap(self, *args): return _rsMDPSlv.map_2str_dbl_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.map_2str_dbl_get_allocator(self)
    def begin(self): return _rsMDPSlv.map_2str_dbl_begin(self)
    def end(self): return _rsMDPSlv.map_2str_dbl_end(self)
    def rbegin(self): return _rsMDPSlv.map_2str_dbl_rbegin(self)
    def rend(self): return _rsMDPSlv.map_2str_dbl_rend(self)
    def count(self, *args): return _rsMDPSlv.map_2str_dbl_count(self, *args)
    def erase(self, *args): return _rsMDPSlv.map_2str_dbl_erase(self, *args)
    def find(self, *args): return _rsMDPSlv.map_2str_dbl_find(self, *args)
    def lower_bound(self, *args): return _rsMDPSlv.map_2str_dbl_lower_bound(self, *args)
    def upper_bound(self, *args): return _rsMDPSlv.map_2str_dbl_upper_bound(self, *args)
    __swig_destroy__ = _rsMDPSlv.delete_map_2str_dbl
    __del__ = lambda self : None;
map_2str_dbl_swigregister = _rsMDPSlv.map_2str_dbl_swigregister
map_2str_dbl_swigregister(map_2str_dbl)

class map_3str_dbl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_3str_dbl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_3str_dbl, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlv.map_3str_dbl_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlv.map_3str_dbl___nonzero__(self)
    def __bool__(self): return _rsMDPSlv.map_3str_dbl___bool__(self)
    def __len__(self): return _rsMDPSlv.map_3str_dbl___len__(self)
    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args): return _rsMDPSlv.map_3str_dbl___getitem__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlv.map_3str_dbl___delitem__(self, *args)
    def has_key(self, *args): return _rsMDPSlv.map_3str_dbl_has_key(self, *args)
    def keys(self): return _rsMDPSlv.map_3str_dbl_keys(self)
    def values(self): return _rsMDPSlv.map_3str_dbl_values(self)
    def items(self): return _rsMDPSlv.map_3str_dbl_items(self)
    def __contains__(self, *args): return _rsMDPSlv.map_3str_dbl___contains__(self, *args)
    def key_iterator(self): return _rsMDPSlv.map_3str_dbl_key_iterator(self)
    def value_iterator(self): return _rsMDPSlv.map_3str_dbl_value_iterator(self)
    def __setitem__(self, *args): return _rsMDPSlv.map_3str_dbl___setitem__(self, *args)
    def asdict(self): return _rsMDPSlv.map_3str_dbl_asdict(self)
    def __init__(self, *args): 
        this = _rsMDPSlv.new_map_3str_dbl(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self): return _rsMDPSlv.map_3str_dbl_empty(self)
    def size(self): return _rsMDPSlv.map_3str_dbl_size(self)
    def clear(self): return _rsMDPSlv.map_3str_dbl_clear(self)
    def swap(self, *args): return _rsMDPSlv.map_3str_dbl_swap(self, *args)
    def get_allocator(self): return _rsMDPSlv.map_3str_dbl_get_allocator(self)
    def begin(self): return _rsMDPSlv.map_3str_dbl_begin(self)
    def end(self): return _rsMDPSlv.map_3str_dbl_end(self)
    def rbegin(self): return _rsMDPSlv.map_3str_dbl_rbegin(self)
    def rend(self): return _rsMDPSlv.map_3str_dbl_rend(self)
    def count(self, *args): return _rsMDPSlv.map_3str_dbl_count(self, *args)
    def erase(self, *args): return _rsMDPSlv.map_3str_dbl_erase(self, *args)
    def find(self, *args): return _rsMDPSlv.map_3str_dbl_find(self, *args)
    def lower_bound(self, *args): return _rsMDPSlv.map_3str_dbl_lower_bound(self, *args)
    def upper_bound(self, *args): return _rsMDPSlv.map_3str_dbl_upper_bound(self, *args)
    __swig_destroy__ = _rsMDPSlv.delete_map_3str_dbl
    __del__ = lambda self : None;
map_3str_dbl_swigregister = _rsMDPSlv.map_3str_dbl_swigregister
map_3str_dbl_swigregister(map_3str_dbl)


def RS_mdp_solver(*args):
  return _rsMDPSlv.RS_mdp_solver(*args)
RS_mdp_solver = _rsMDPSlv.RS_mdp_solver
# This file is compatible with both classic and new-style classes.


