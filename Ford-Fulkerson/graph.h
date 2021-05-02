#include <vector>

#ifndef GRAPH_H
#define GRAPH_H

typedef std::vector <int> v;
typedef std::vector <v> adj;

struct graph
{
    int V;
    int E;
    adj adj_list;
} typedef Graph;

#endif /* GRAPH_H */
