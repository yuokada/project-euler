object Hello {

  def main(args: Array[String]) = {
    val ar = 1 to 100
    val sqsum = ar.map{x => x * x}.sum
    val sq = ar.sum * ar.sum
    println(sq - sqsum)
  }
}
