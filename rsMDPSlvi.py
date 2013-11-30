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
            fp, pathname, description = imp.find_module('_rsMDPSlvi', [dirname(__file__)])
        except ImportError:
            import _rsMDPSlvi
            return _rsMDPSlvi
        if fp is not None:
            try:
                _mod = imp.load_module('_rsMDPSlvi', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rsMDPSlvi = swig_import_helper()
    del swig_import_helper
else:
    import _rsMDPSlvi
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
    __swig_destroy__ = _rsMDPSlvi.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _rsMDPSlvi.SwigPyIterator_value(self)
    def incr(self, n=1): return _rsMDPSlvi.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _rsMDPSlvi.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _rsMDPSlvi.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _rsMDPSlvi.SwigPyIterator_equal(self, *args)
    def copy(self): return _rsMDPSlvi.SwigPyIterator_copy(self)
    def next(self): return _rsMDPSlvi.SwigPyIterator_next(self)
    def __next__(self): return _rsMDPSlvi.SwigPyIterator___next__(self)
    def previous(self): return _rsMDPSlvi.SwigPyIterator_previous(self)
    def advance(self, *args): return _rsMDPSlvi.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _rsMDPSlvi.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _rsMDPSlvi.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _rsMDPSlvi.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _rsMDPSlvi.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _rsMDPSlvi.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _rsMDPSlvi.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _rsMDPSlvi.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vec1i(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec1i, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec1i, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec1i_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec1i___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec1i___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec1i___len__(self)
    def pop(self): return _rsMDPSlvi.vec1i_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec1i___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec1i___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec1i___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec1i___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec1i___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec1i___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec1i_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec1i_empty(self)
    def size(self): return _rsMDPSlvi.vec1i_size(self)
    def clear(self): return _rsMDPSlvi.vec1i_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec1i_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec1i_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec1i_begin(self)
    def end(self): return _rsMDPSlvi.vec1i_end(self)
    def rbegin(self): return _rsMDPSlvi.vec1i_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec1i_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec1i_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec1i_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec1i(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec1i_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec1i_front(self)
    def back(self): return _rsMDPSlvi.vec1i_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec1i_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec1i_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec1i_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec1i_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec1i_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec1i
    __del__ = lambda self : None;
vec1i_swigregister = _rsMDPSlvi.vec1i_swigregister
vec1i_swigregister(vec1i)

class vec2i(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec2i, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec2i, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec2i_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec2i___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec2i___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec2i___len__(self)
    def pop(self): return _rsMDPSlvi.vec2i_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec2i___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec2i___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec2i___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec2i___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec2i___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec2i___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec2i_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec2i_empty(self)
    def size(self): return _rsMDPSlvi.vec2i_size(self)
    def clear(self): return _rsMDPSlvi.vec2i_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec2i_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec2i_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec2i_begin(self)
    def end(self): return _rsMDPSlvi.vec2i_end(self)
    def rbegin(self): return _rsMDPSlvi.vec2i_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec2i_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec2i_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec2i_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec2i(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec2i_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec2i_front(self)
    def back(self): return _rsMDPSlvi.vec2i_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec2i_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec2i_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec2i_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec2i_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec2i_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec2i
    __del__ = lambda self : None;
vec2i_swigregister = _rsMDPSlvi.vec2i_swigregister
vec2i_swigregister(vec2i)

class vec3i(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec3i, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec3i, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec3i_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec3i___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec3i___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec3i___len__(self)
    def pop(self): return _rsMDPSlvi.vec3i_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec3i___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec3i___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec3i___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec3i___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec3i___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec3i___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec3i_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec3i_empty(self)
    def size(self): return _rsMDPSlvi.vec3i_size(self)
    def clear(self): return _rsMDPSlvi.vec3i_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec3i_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec3i_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec3i_begin(self)
    def end(self): return _rsMDPSlvi.vec3i_end(self)
    def rbegin(self): return _rsMDPSlvi.vec3i_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec3i_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec3i_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec3i_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec3i(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec3i_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec3i_front(self)
    def back(self): return _rsMDPSlvi.vec3i_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec3i_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec3i_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec3i_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec3i_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec3i_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec3i
    __del__ = lambda self : None;
vec3i_swigregister = _rsMDPSlvi.vec3i_swigregister
vec3i_swigregister(vec3i)

class vec1s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec1s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec1s, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec1s_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec1s___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec1s___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec1s___len__(self)
    def pop(self): return _rsMDPSlvi.vec1s_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec1s___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec1s___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec1s___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec1s___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec1s___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec1s___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec1s_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec1s_empty(self)
    def size(self): return _rsMDPSlvi.vec1s_size(self)
    def clear(self): return _rsMDPSlvi.vec1s_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec1s_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec1s_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec1s_begin(self)
    def end(self): return _rsMDPSlvi.vec1s_end(self)
    def rbegin(self): return _rsMDPSlvi.vec1s_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec1s_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec1s_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec1s_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec1s(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec1s_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec1s_front(self)
    def back(self): return _rsMDPSlvi.vec1s_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec1s_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec1s_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec1s_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec1s_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec1s_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec1s
    __del__ = lambda self : None;
vec1s_swigregister = _rsMDPSlvi.vec1s_swigregister
vec1s_swigregister(vec1s)

class vec2s(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec2s, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec2s, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec2s_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec2s___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec2s___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec2s___len__(self)
    def pop(self): return _rsMDPSlvi.vec2s_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec2s___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec2s___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec2s___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec2s___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec2s___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec2s___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec2s_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec2s_empty(self)
    def size(self): return _rsMDPSlvi.vec2s_size(self)
    def clear(self): return _rsMDPSlvi.vec2s_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec2s_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec2s_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec2s_begin(self)
    def end(self): return _rsMDPSlvi.vec2s_end(self)
    def rbegin(self): return _rsMDPSlvi.vec2s_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec2s_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec2s_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec2s_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec2s(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec2s_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec2s_front(self)
    def back(self): return _rsMDPSlvi.vec2s_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec2s_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec2s_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec2s_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec2s_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec2s_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec2s
    __del__ = lambda self : None;
vec2s_swigregister = _rsMDPSlvi.vec2s_swigregister
vec2s_swigregister(vec2s)

class vec1d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec1d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec1d, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec1d_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec1d___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec1d___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec1d___len__(self)
    def pop(self): return _rsMDPSlvi.vec1d_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec1d___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec1d___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec1d___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec1d___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec1d___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec1d___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec1d_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec1d_empty(self)
    def size(self): return _rsMDPSlvi.vec1d_size(self)
    def clear(self): return _rsMDPSlvi.vec1d_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec1d_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec1d_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec1d_begin(self)
    def end(self): return _rsMDPSlvi.vec1d_end(self)
    def rbegin(self): return _rsMDPSlvi.vec1d_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec1d_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec1d_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec1d_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec1d(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec1d_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec1d_front(self)
    def back(self): return _rsMDPSlvi.vec1d_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec1d_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec1d_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec1d_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec1d_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec1d_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec1d
    __del__ = lambda self : None;
vec1d_swigregister = _rsMDPSlvi.vec1d_swigregister
vec1d_swigregister(vec1d)

class vec2d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec2d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec2d, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec2d_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec2d___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec2d___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec2d___len__(self)
    def pop(self): return _rsMDPSlvi.vec2d_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec2d___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec2d___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec2d___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec2d___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec2d___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec2d___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec2d_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec2d_empty(self)
    def size(self): return _rsMDPSlvi.vec2d_size(self)
    def clear(self): return _rsMDPSlvi.vec2d_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec2d_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec2d_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec2d_begin(self)
    def end(self): return _rsMDPSlvi.vec2d_end(self)
    def rbegin(self): return _rsMDPSlvi.vec2d_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec2d_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec2d_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec2d_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec2d(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec2d_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec2d_front(self)
    def back(self): return _rsMDPSlvi.vec2d_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec2d_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec2d_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec2d_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec2d_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec2d_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec2d
    __del__ = lambda self : None;
vec2d_swigregister = _rsMDPSlvi.vec2d_swigregister
vec2d_swigregister(vec2d)

class vec3d(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vec3d, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vec3d, name)
    __repr__ = _swig_repr
    def iterator(self): return _rsMDPSlvi.vec3d_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _rsMDPSlvi.vec3d___nonzero__(self)
    def __bool__(self): return _rsMDPSlvi.vec3d___bool__(self)
    def __len__(self): return _rsMDPSlvi.vec3d___len__(self)
    def pop(self): return _rsMDPSlvi.vec3d_pop(self)
    def __getslice__(self, *args): return _rsMDPSlvi.vec3d___getslice__(self, *args)
    def __setslice__(self, *args): return _rsMDPSlvi.vec3d___setslice__(self, *args)
    def __delslice__(self, *args): return _rsMDPSlvi.vec3d___delslice__(self, *args)
    def __delitem__(self, *args): return _rsMDPSlvi.vec3d___delitem__(self, *args)
    def __getitem__(self, *args): return _rsMDPSlvi.vec3d___getitem__(self, *args)
    def __setitem__(self, *args): return _rsMDPSlvi.vec3d___setitem__(self, *args)
    def append(self, *args): return _rsMDPSlvi.vec3d_append(self, *args)
    def empty(self): return _rsMDPSlvi.vec3d_empty(self)
    def size(self): return _rsMDPSlvi.vec3d_size(self)
    def clear(self): return _rsMDPSlvi.vec3d_clear(self)
    def swap(self, *args): return _rsMDPSlvi.vec3d_swap(self, *args)
    def get_allocator(self): return _rsMDPSlvi.vec3d_get_allocator(self)
    def begin(self): return _rsMDPSlvi.vec3d_begin(self)
    def end(self): return _rsMDPSlvi.vec3d_end(self)
    def rbegin(self): return _rsMDPSlvi.vec3d_rbegin(self)
    def rend(self): return _rsMDPSlvi.vec3d_rend(self)
    def pop_back(self): return _rsMDPSlvi.vec3d_pop_back(self)
    def erase(self, *args): return _rsMDPSlvi.vec3d_erase(self, *args)
    def __init__(self, *args): 
        this = _rsMDPSlvi.new_vec3d(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _rsMDPSlvi.vec3d_push_back(self, *args)
    def front(self): return _rsMDPSlvi.vec3d_front(self)
    def back(self): return _rsMDPSlvi.vec3d_back(self)
    def assign(self, *args): return _rsMDPSlvi.vec3d_assign(self, *args)
    def resize(self, *args): return _rsMDPSlvi.vec3d_resize(self, *args)
    def insert(self, *args): return _rsMDPSlvi.vec3d_insert(self, *args)
    def reserve(self, *args): return _rsMDPSlvi.vec3d_reserve(self, *args)
    def capacity(self): return _rsMDPSlvi.vec3d_capacity(self)
    __swig_destroy__ = _rsMDPSlvi.delete_vec3d
    __del__ = lambda self : None;
vec3d_swigregister = _rsMDPSlvi.vec3d_swigregister
vec3d_swigregister(vec3d)


def RS_mdp_solver(*args):
  return _rsMDPSlvi.RS_mdp_solver(*args)
RS_mdp_solver = _rsMDPSlvi.RS_mdp_solver
# This file is compatible with both classic and new-style classes.


