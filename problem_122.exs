defmodule Problem do 
  
  # def cache_put(cache, produce, known, steps) do
  #   Map.put(
  #     cache,
  #     produce,
  #     Map.put(
  #       if cache[produce] == nil do
  #         %{}
  #       else
  #         cache[produce]
  #       end,
  #       Enum.filter(known, &(&1 <= produce)),
  #       steps
  #     )
  #   )
  # end

  # # Produce is the value we're trying to make
  # # Known is all the exponents we already have "computed"
  # # Cache is mapping from produce -> known lte produce -> min 
  # def find(produce, known, cache) do
  #   ## IO.inspect produce
  #   ## IO.inspect known
  #   ## IO.inspect cache
  #   ## # Cache hit.
  #   known_lt = Enum.filter(known, &(&1 <= produce))
  #   if false do # cache[produce][known_lt] != nil do
  #     ## IO.puts "cache hit"
  #     {cache[produce][known_lt], known, cache}
  #   else
  #     # Has membership.
  #     if MapSet.member?(known, produce) or produce <= 1 do
  #       ## IO.puts "member"
  #       new_known = known |> MapSet.put(1)
  #       {0, new_known, cache_put(cache, produce, new_known, 0)}
  #     else
  #       1..(produce - 1)
  #       |> Enum.reduce(
  #         {-1, MapSet.new(), %{}},
  #         fn(val, acc) ->
  #           {prevmin, _, _} = acc
  #           {lsteps, left_known, left_cache} = find(val, known, cache)
  #           {rsteps, right_known, right_cache} = find(produce - val, left_known, left_cache)
  #           dfkjldsflkslaq otal_steps = lsteps + rsteps + 1
  #           new_known = MapSet.union(left_known, right_known) |> MapSet.put(produce)
  #           # if produce == 5 do IO.puts "total steps #{total_steps} #{prevmin}" end
  #           if total_steps < prevmin or prevmin == -1 do
  #             new_cache = cache_put(right_cache, produce, new_known, total_steps)
  #             {total_steps, new_known, new_cache}
  #           else
  #             acc
  #           end
  #         end
  #       )
  #     end
  #   end
  # end

  # def find_up(n) do
  #   Enum.reduce(
  #     1..n,
  #     %{},
  #     fn(val, cache) ->
  #       {st, _, new_cache} = find(val, MapSet.new(), cache)
  #       IO.puts "VAL #{val} ST #{st} CACHE"
  #       IO.inspect cache
  #       new_cache
  #     end
  #   )
  # end
  #
  #
  #
  def generate_j(item, lst, []) do
    []
  end

  def generate_j(item, lst, [head | tail]) do
    [Enum.uniq([item + head | lst])] # | generate_j(item, lst, tail)]
  end
  
  def generate_h(lst, []) do
    [lst]
  end

  def generate_h(lst, [head | tail]) do
    generate_j(head, lst, lst) ++ generate_h(lst, tail)
  end

  def generate(lst) do
    Enum.uniq(generate_h(lst, lst))
  end

  def forward(n, [head | tail]) do
    if List.first(head) == n do
      head
    else
      if List.first(head) > n do
        forward(n, tail)
      else
        forward(n, tail ++ generate(head))
      end
    end
  end

end

# IO.inspect Problem.find_up(16)
# IO.inspect Problem.generate([2, 1])
IO.inspect Problem.forward(200, [[1]])
